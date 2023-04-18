import re
import random

from django.conf import settings
from django.db import transaction
from django_redis import get_redis_connection

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from . import models
from .tasks import send_sms
from .models import UserCourse, StudyProgress
from course.models import Course, CourseLesson
from .serializers import (
    UserRegisterModelSerializer, UserLoginSMSModelSerializer, UserCourseModelSerializer
)

from logger import log
from constants import MAV_SEEK_TIME
from response import APIResponse
from return_code import (
    SUCCESS, AUTH_FAILED, TOO_MANY_REQUESTS, SERVER_ERROR, VALIDATE_ERROR, HTTP_400_BAD_REQUEST
)
from mixins import ReCreateModelMixin, ReListModelMixin
from paginations import RePageNumberPagination


class MobileAPIView(APIView):
    def get(self, request, mobile, *args, **kwargs):
        """
        校验手机号是否已注册
        :param request:
        :param mobile: 手机号
        :return:
        """
        # 验证手机号格式
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            return APIResponse(AUTH_FAILED, "手机号格式错误.")
        # 查看验证码是否注册
        if models.UserInfo.objects.filter(mobile=mobile).exists():
            return APIResponse(AUTH_FAILED, "手机号已注册.")
        else:
            return APIResponse(SUCCESS, "手机号尚未注册,请安全注册.")


class UserRegisterGenericAPIView(GenericViewSet, ReCreateModelMixin):
    queryset = models.UserInfo.objects.filter(is_deleted=False)
    serializer_class = UserRegisterModelSerializer


class SMSAPIView(APIView):
    """
    SMS短信接口视图
    """

    def get(self, request, mobile):
        """发送短信验证码"""

        # 验证手机号格式
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            return APIResponse(AUTH_FAILED, "手机号格式错误.")

        redis = get_redis_connection("sms_code")
        # 判断手机短信是否处于发送冷却中[60秒只能发送一条]
        interval = redis.ttl(f"interval_{mobile}")  # 通过ttl方法可以获取保存在redis中的变量的剩余有效期
        if interval != -2:
            return APIResponse(TOO_MANY_REQUESTS, f"短信发送过于频繁，请{interval}秒后再次点击获取!")

        # 基于随机数生成短信验证码
        code = f"{random.randint(0, 9999):04d}"

        # 获取短信有效期的时间
        time = settings.RONGLIANYUN.get("sms_expire")
        # 短信发送间隔时间
        sms_interval = settings.RONGLIANYUN["sms_interval"]

        # 调用第三方sdk异步发送短信
        is_ok = send_sms.delay(settings.RONGLIANYUN.get("reg_tid"), mobile, datas=(code, time // 60))

        # 判断验证码是否接入成功
        if not is_ok:
            return APIResponse(SERVER_ERROR, "验证码接入错误.")

        # 记录code到redis中，并以time作为有效期
        # 使用redis提供的管道对象pipeline来优化redis的写入操作[添加/修改/删除]
        pipe = redis.pipeline()
        pipe.multi()  # 开启事务
        pipe.setex(f"sms_{mobile}", time, code)
        pipe.setex(f"interval_{mobile}", sms_interval, "_")
        pipe.execute()  # 提交事务，同时把暂存在pipeline的数据一次性提交给redis

        return APIResponse(message="验证码发送成功.")


class UserLoginSMSGenericAPIView(APIView):
    """手机号短信验证码登录"""
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSMSModelSerializer(data=request.data)
        if not serializer.is_valid():
            return APIResponse(VALIDATE_ERROR, serializer.errors)
        return APIResponse(data=serializer.data)


class CourseListAPIView(ReListModelMixin, GenericViewSet):
    """当前用户的课程列表信息"""
    permission_classes = [IsAuthenticated]
    pagination_class = RePageNumberPagination

    serializer_class = UserCourseModelSerializer

    def get_queryset(self):
        user = self.request.user
        query = UserCourse.objects.filter(user=user)
        course_type = int(self.request.query_params.get("type", -1))
        course_type_list = [item[0] for item in Course.course_type_choices]
        if course_type in course_type_list:
            query = query.filter(course__course_type=course_type)
        return query.order_by("-id").all()


class UserCourseAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserCourseModelSerializer

    def get(self, request, course_id):
        """获取用户在当前课程的学习进度"""
        user = request.user
        try:
            user_course = UserCourse.objects.get(user=user, course=course_id)
        except UserCourse.DoesNotExist:
            return APIResponse(HTTP_400_BAD_REQUEST, "当前课程您尚未购买.")

        chapter_id = user_course.chapter_id
        if chapter_id:
            """曾经学习过本课程"""
            lesson = user_course.lesson
        else:
            """从未学习当前课程"""
            # 获取当前课程第1个章节
            chapter = user_course.course.chapter_list.order_by("orders").first()
            # 获取当前章节第1个课时
            lesson = chapter.lesson_list.order_by("orders").first()
            # 保存本次学习起始进度
            user_course.chapter = chapter
            user_course.lesson = lesson
            user_course.save()

        serializer = self.get_serializer(user_course)
        data = serializer.data
        # 获取当前课时的课时类型和课时链接
        data["lesson_type"] = lesson.lesson_type
        data["lesson_link"] = lesson.lesson_link

        return APIResponse(data=data)


class StudyLessonAPIView(APIView):
    """用户在当前课时的学习时间进度"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        lesson_id = int(request.query_params.get("lesson"))
        user = request.user

        # 查找课时
        lesson = CourseLesson.objects.get(pk=lesson_id)

        progress = StudyProgress.objects.filter(user=user, lesson=lesson).first()

        # 如果查询没有进度，则默认进度为0
        if progress is None:
            progress = StudyProgress.objects.create(
                user=request.user,
                lesson=lesson,
                study_time=0
            )

        return APIResponse(data=progress.study_time)


class StudyProgressAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """添加课时学习进度"""
        try:
            # 1. 接收客户端提交的视频进度和课时ID
            study_time = int(request.data.get("time"))
            lesson_id = int(request.data.get("lesson"))
            user = request.user

            # 判断当前课时是否免费或者当前课时所属的课程是否被用户购买了

            # 判断本次更新学习时间是否超出阈值，当超过阈值，则表示用户已经违规快进了。
            if study_time > MAV_SEEK_TIME:
                raise Exception

            # 查找课时
            lesson = CourseLesson.objects.get(pk=lesson_id)

        except:

            return APIResponse(HTTP_400_BAD_REQUEST, "无效的参数或当前课程信息不存在.")

        with transaction.atomic():
            save_id = transaction.savepoint()
            try:
                # 2. 记录课时学习进度
                progress = StudyProgress.objects.filter(user=user, lesson=lesson).first()

                if progress is None:
                    """新增一条用户与课时的学习记录"""
                    progress = StudyProgress(
                        user=user,
                        lesson=lesson,
                        study_time=study_time
                    )
                else:
                    """直接更新现有的学习时间"""
                    progress.study_time = int(progress.study_time) + int(study_time)

                progress.save()

                # 3. 记录课程学习的总进度
                user_course = UserCourse.objects.get(user=user, course=lesson.course)
                user_course.study_time = int(user_course.study_time) + int(study_time)

                # 4. 记录用户正在查看的章节和课时
                # 用户如果往后观看章节，则记录下
                if lesson.chapter.orders > user_course.chapter.orders:
                    user_course.chapter = lesson.chapter
                # 用户如果往后观看课时，则记录下
                if lesson.orders > user_course.lesson.orders:
                    user_course.lesson = lesson

                user_course.save()

                return APIResponse(message="课时学习进度更新完成.")

            except Exception as e:

                log.error(f"更新课时进度失败.---{e}")
                transaction.savepoint_rollback(save_id)
                return APIResponse(message="当前课时学习进度丢失.")


class UserInfoAPIView(APIView):
    """用户个人信息"""
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.user.id

        user_obj = models.UserInfo.objects.filter(pk=user_id, is_deleted=False)
        if not user_obj.exists():
            return APIResponse(HTTP_400_BAD_REQUEST, "用户不存在.")

        user_obj = user_obj.first()
        user_data = {
            "user_id": user_obj.id,
            "username": user_obj.username,
            "mobile": user_obj.mobile,
            "money": float(user_obj.money),
            "credit": user_obj.credit,
            "avatar": user_obj.avatar.url,
            "nickname": user_obj.nickname,
            "study_time": user_obj.study_time,
            "email": user_obj.email,
            "last_login": user_obj.last_login,
        }
        # print("user_data", user_data)
        return APIResponse(data=user_data)

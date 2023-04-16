import re

from django.conf import settings
from django_redis import get_redis_connection

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models
from .models import UserCourse

from authenticate import generate_jwt_token


class UserRegisterModelSerializer(serializers.ModelSerializer):
    """
    注册功能
    """
    re_password = serializers.CharField(required=True, write_only=True)
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = models.UserInfo
        fields = ("mobile", "password", "re_password", "sms_code", "token")
        extra_kwargs = {
            "mobile": {
                "required": True, "write_only": True
            },
            "password": {
                "required": True, "write_only": True, "min_length": 8, "max_length": 18,
            },
        }

    def validate(self, attrs):
        # 验证手机号格式
        mobile = attrs.get("mobile")
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            raise ValidationError("手机号格式错误.")

        # 验证码两次密码是否一致
        password = attrs.get("password")
        re_password = attrs.get("re_password")
        if password != re_password:
            raise ValidationError("两次密码不一致.")

        # 查看验证码是否注册
        if models.UserInfo.objects.filter(mobile=mobile).exists():
            raise ValidationError("手机号已注册.")

        # 从redis中提取短信
        redis = get_redis_connection("sms_code")
        code = redis.get(f"sms_{mobile}")
        if code is None:
            # 获取不到验证码，则表示验证码已经过期了或未发送验证码
            raise ValidationError(detail="验证码不存在或已过期.", code="sms_code")
        # 从redis提取的数据，字符串都是bytes类型，所以decode
        if code.decode() != attrs.get("sms_code"):
            raise ValidationError(detail="短信验证码错误.", code="sms_code")
        # 删除掉redis中的短信和短信失效时间
        redis.delete(f"sms_{mobile}")
        redis.delete(f"interval_{mobile}")

        return attrs

    def create(self, validated_data):
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")
        user = models.UserInfo.objects.create_user(
            username=mobile,
            mobile=mobile,
            password=password,
            avatar=settings.DEFAULT_USER_AVATAR,
        )
        user.token = generate_jwt_token(user)
        return user


class UserLoginSMSModelSerializer(serializers.ModelSerializer):
    """
    手机号短信登录
    """
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True)
    token = serializers.CharField(read_only=True)
    mobile = serializers.CharField(required=True, write_only=True)

    username = serializers.CharField(required=False, read_only=True)
    money = serializers.IntegerField(required=False, read_only=True)
    credit = serializers.IntegerField(required=False, read_only=True)
    nickname = serializers.CharField(required=False, read_only=True)
    study_time = serializers.CharField(required=False, read_only=True)
    email = serializers.CharField(required=False, read_only=True)
    last_login = serializers.DateTimeField(required=False, read_only=True)
    avatar = serializers.CharField(required=False, read_only=True)
    cart_total = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = models.UserInfo
        fields = (
            "mobile", "sms_code", "token",

            "username", "money", "credit",
            "nickname", "study_time", "email",
            "last_login", "avatar", "cart_total",
        )

    def validate(self, attrs):
        # 验证手机号格式
        mobile = attrs.get("mobile")
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            raise ValidationError("手机号格式错误.")

        # 校验验证码
        sms_code = attrs.get("sms_code")
        if not sms_code:
            raise ValidationError("请输入验证码.")

        # 校验手机号是否存在
        user = models.UserInfo.objects.filter(mobile=mobile)
        if not user.exists():
            raise ValidationError("手机号尚未注册.")

        # 从redis中提取短信
        redis = get_redis_connection("sms_code")
        code = redis.get(f"sms_{mobile}")
        if code is None:
            # 获取不到验证码，则表示验证码已经过期了或未发送验证码
            raise ValidationError(detail="验证码不存在或已过期.", code="sms_code")
        # 从redis提取的数据，字符串都是bytes类型，所以decode
        if code.decode() != attrs.get("sms_code"):
            raise ValidationError(detail="短信验证码错误.", code="sms_code")
        # 删除掉redis中的短信和短信失效时间
        redis.delete(f"sms_{mobile}")
        redis.delete(f"interval_{mobile}")

        user = user.first()

        # 返回token
        user.token = generate_jwt_token(user)

        # 购物车数量
        redis = get_redis_connection("cart")
        cart_total = redis.hlen(f"cart_{user.id}")
        user.cart_total = cart_total

        return user


class UserCourseModelSerializer(serializers.ModelSerializer):
    """用户课程信息序列化器"""
    course_cover = serializers.ImageField(source="course.course_cover")
    course_name = serializers.CharField(source="course.name")
    chapter_name = serializers.CharField(source="chapter.name", default="")
    chapter_id = serializers.IntegerField(source="chapter.id", default=0)
    chapter_orders = serializers.IntegerField(source="chapter.orders", default=0)
    lesson_id = serializers.IntegerField(source="lesson.id", default=0)
    lesson_name = serializers.CharField(source="lesson.name", default="")
    lesson_orders = serializers.IntegerField(source="lesson.orders", default=0)
    course_type = serializers.IntegerField(source="course.course_type", default=0)
    get_course_type_display = serializers.CharField(source="course.get_course_type_display", default="")

    class Meta:
        model = UserCourse
        fields = [
            "course_id", "course_cover", "course_name", "study_time",
            "chapter_id", "chapter_orders", "chapter_name",
            "lesson_id", "lesson_orders", "lesson_name",
            "course_type", "get_course_type_display", "progress",
            "note", "qa", "code"
        ]

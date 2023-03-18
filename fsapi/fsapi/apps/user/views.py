import re
import random

from django.conf import settings
from django_redis import get_redis_connection

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from . import models
from .serializers import UserRegisterModelSerializer

from response import APIResponse
from return_code import SUCCESS, AUTH_FAILED, TOO_MANY_REQUESTS, SERVER_ERROR
from mixins import ReCreateModelMixin
from sms.ronglianyunapi import send_sms


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
        # 查看验证码是否注册
        if models.UserInfo.objects.filter(mobile=mobile).exists():
            return APIResponse(AUTH_FAILED, "手机号已注册.")

        redis = get_redis_connection("sms_code")
        # 判断手机短信是否处于发送冷却中[60秒只能发送一条]
        interval = redis.ttl(f"interval_{mobile}")  # 通过ttl方法可以获取保存在redis中的变量的剩余有效期
        if interval != -2:
            return APIResponse(TOO_MANY_REQUESTS, f"短信发送过于频繁，请{interval}秒后再次点击获取!")

        # 基于随机数生成短信验证码
        code = f"{random.randint(0, 999999):06d}"
        # 获取短信有效期的时间
        time = settings.RONGLIANYUN.get("sms_expire")
        # 短信发送间隔时间
        sms_interval = settings.RONGLIANYUN["sms_interval"]
        # 调用第三方sdk发送短信
        is_ok = send_sms(settings.RONGLIANYUN.get("reg_tid"), mobile, datas=(code, time // 60))
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

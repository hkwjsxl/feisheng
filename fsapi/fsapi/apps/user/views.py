import re

from rest_framework.views import APIView

from response import APIResponse
from return_code import SUCCESS, AUTH_FAILED
from . import models


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
            return APIResponse(SUCCESS, "注册成功.")

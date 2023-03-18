import re

from django.conf import settings
from django_redis import get_redis_connection

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models

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

    class Meta:
        model = models.UserInfo
        fields = ("mobile", "sms_code", "token")

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

        return user

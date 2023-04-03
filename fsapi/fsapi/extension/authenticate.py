from django.db.models import Q
from django.contrib.auth.backends import ModelBackend, UserModel

from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework_jwt.settings import api_settings
from django_redis import get_redis_connection


def custom_jwt_payload_handler(user):
    """
    自定义载荷信息
    :params user  用户模型实例对象
    """
    # 先让jwt模块生成自己的载荷信息
    payload = jwt_payload_handler(user)
    # 追加自己要返回的字段内容
    if hasattr(user, 'avatar'):
        payload['avatar'] = user.avatar.url if user.avatar else ""
    if hasattr(user, 'nickname'):
        payload['nickname'] = user.nickname
    if hasattr(user, 'money'):
        payload['money'] = float(user.money)
    if hasattr(user, 'credit'):
        payload['credit'] = user.credit

    return payload


def get_user_by_account(account):
    """
    根据帐号信息获取user模型实例对象
    :param account: 账号信息，可以是用户名，也可以是手机号，甚至其他的可用于识别用户身份的字段信息
    :return: User对象 或者 None
    """
    user = UserModel.objects.filter(Q(mobile=account) | Q(username=account) | Q(email=account)).first()
    return user


class CustomAuthBackend(ModelBackend):
    """
    自定义用户认证类[实现多条件登录]
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        多条件认证方法
        :param request: 本次客户端的http请求对象
        :param username:  本次客户端提交的用户信息，可以是user，也可以mobile或其他唯一字段
        :param password: 本次客户端提交的用户密码
        :param kwargs: 额外参数
        :return:
        """
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        if username is None or password is None:
            return
        # 根据用户名信息useranme获取账户信息
        user = get_user_by_account(username)
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user


def generate_jwt_token(user):
    """
    生成jwt token
    @params user: 用户模型实例对象
    """
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)


def jwt_response_payload_handler(token, user, request):
    """
    控制JWT返回的格式
    """
    redis = get_redis_connection("cart")
    cart_total = redis.hlen(f"cart_{user.id}")

    return {
        # 增加返回购物车的商品数量
        "cart_total": cart_total,
        "token": token
    }

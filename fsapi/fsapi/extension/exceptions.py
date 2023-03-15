from redis import RedisError
from django.db import DatabaseError

from rest_framework.views import exception_handler
from rest_framework import status

from fsapi.extension.response import APIResponse
from fsapi.extension.logger import log

def custom_exception_handler(exc, context):
    """
    自定义异常处理
    :param exc: 异常类
    :param context: 抛出异常的上下文
    :return: Response响应对象
    """
    # 调用drf框架原生的异常处理方法
    response = exception_handler(exc, context)
    if not response:
        view = context['view']
        if isinstance(exc, DatabaseError):
            # mysql数据库异常
            response = APIResponse(status.HTTP_507_INSUFFICIENT_STORAGE, "MySQL数据库内部错误")
        elif isinstance(exc, RedisError):
            # redis数据库异常
            response = APIResponse(status.HTTP_507_INSUFFICIENT_STORAGE, "Redis数据库异常")
        try:
            if isinstance(response.data, list):
                response= APIResponse(status.HTTP_500_INTERNAL_SERVER_ERROR, response.data)
            else:
                response = APIResponse(status.HTTP_500_INTERNAL_SERVER_ERROR, response.data.get('detail') or response.data)
        except AttributeError:
            # 处理resposne没有data属性的情况
            return APIResponse(status.HTTP_500_INTERNAL_SERVER_ERROR, '[%s] %s' % (view, exc))
    log.error('[%s] %s' % (view, exc))
    return response

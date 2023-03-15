from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.viewsets import GenericViewSet

from mixins import ReListModelMixin
from constants import LIST_PAGE_CACHE_TIME


class CacheListAPIView(ReListModelMixin, GenericViewSet):
    """列表缓存视图"""

    @method_decorator(cache_page(LIST_PAGE_CACHE_TIME))
    def list(self, request, *args, **kwargs):
        # 只是加上了缓存装饰器，其他什么都不用干
        return super().list(request, *args, **kwargs)

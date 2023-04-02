from datetime import datetime, timedelta

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from rest_framework.generics import GenericAPIView
from rest_framework.filters import OrderingFilter
from django_filters import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_haystack.filters import HaystackFilter
from drf_haystack.generics import HaystackGenericAPIView
from django_redis import get_redis_connection

from .models import CourseDirection, CourseCategory, Course
from .serializers import (
    CourseDirectionModelSerializer, CourseCategoryModelSerializer, CourseInfoModelSerializer,
    CourseIndexHaystackSerializer, CourseRetrieveModelSerializer
)

import constants
from mixins import ReListModelMixin, ReRetrieveModelMixin
from paginations import RePageNumberPagination
from response import APIResponse


class CourseDirectionGenericAPIView(GenericViewSet, ReListModelMixin):
    """学习方向"""
    queryset = CourseDirection.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseDirectionModelSerializer
    pagination_class = None


class CourseCategoryFilterSet(FilterSet):
    """
    获取方向下的全部分类
    http://127.0.0.1:8000/course/category/?direction=10
    """
    direction = filters.CharFilter(field_name='direction', label='课程分类名称')

    class Meta:
        model = CourseCategory
        fields = ('direction',)


class CourseCategoryGenericAPIView(GenericViewSet, ReListModelMixin):
    """课程分类"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CourseCategoryFilterSet
    pagination_class = None

    queryset = CourseCategory.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseCategoryModelSerializer


class CourseInfoFilterSet(FilterSet):
    """
    课程列表筛选
    http://127.0.0.1:8000/course/
    http://127.0.0.1:8000/course/?direction=1&category=2
    """
    direction = filters.CharFilter(field_name='direction', label='课程方向')
    category = filters.CharFilter(field_name='category', label='课程分类')

    class Meta:
        model = Course
        fields = ("direction", "category",)


class CourseInfoGenericAPIView(GenericViewSet, ReListModelMixin):
    """
    课程列表接口
    排序：http://127.0.0.1:8000/course/?ordering=-students
    分页：http://127.0.0.1:8000/course/?page=2&size=2
    """
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CourseInfoFilterSet
    ordering_fields = ('id', 'students', 'orders')
    pagination_class = RePageNumberPagination

    queryset = Course.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseInfoModelSerializer


class CourseSearchViewSet(ReRetrieveModelMixin, ReListModelMixin, ViewSetMixin, HaystackGenericAPIView):
    """课程信息全文搜索视图类"""
    # 指定本次搜索的最终真实数据的保存模型
    index_models = [Course]
    serializer_class = CourseIndexHaystackSerializer
    filter_backends = [OrderingFilter, HaystackFilter]
    ordering_fields = ('id', 'students', 'orders')
    pagination_class = RePageNumberPagination

    def list(self, request, *args, **kwargs):
        # 保存本次搜索的关键字
        redis = get_redis_connection("hot_word")
        text = request.query_params.get("text")
        if text:
            key = f"{constants.DEFAULT_HOT_WORD}:{datetime.now().strftime('%Y:%m:%d')}"
            is_exists = redis.exists(key)
            # 让有序集合中的text搜索关键字次数+1，如果该关键字第一次出现，则为1
            redis.zincrby(key, 1, text)
            if not is_exists:
                redis.expire(key, constants.HOT_WORD_EXPIRE * 24 * 3600)

        return super().list(request, *args, **kwargs)


class HotWordAPIView(APIView):
    """搜索热词"""

    def get(self, request):
        redis = get_redis_connection("hot_word")
        # 获取最近指定天数的热词的key
        date_list = []
        for i in range(0, constants.HOT_WORD_EXPIRE):
            day = datetime.now() - timedelta(days=i)
            months = day.month if day.month >= 10 else f"0{day.month}"
            days = day.day if day.day >= 10 else f"0{day.day}"
            key = f"{constants.DEFAULT_HOT_WORD}:{day.year}:{months}:{days}"
            date_list.append(key)
        # 先删除原有的统计最近几天的热搜词的有序统计集合
        redis.delete(constants.DEFAULT_HOT_WORD)
        # 根据date_list找到最近指定天数的所有集合，并完成并集计算，产生新的有序统计集合constants.DEFAULT_HOT_WORD
        redis.zunionstore(constants.DEFAULT_HOT_WORD, date_list, aggregate="sum")
        # 按分数store进行倒序显示排名靠前的指定数量的热词
        word_list = redis.zrevrange(constants.DEFAULT_HOT_WORD, 0, constants.HOT_WORD_LENGTH - 1)
        return APIResponse(data=word_list)


class CourseRetrieveAPIView(ReRetrieveModelMixin, GenericAPIView):
    """课程详情信息"""
    queryset = Course.objects.filter(is_show=True, is_deleted=False).all()
    serializer_class = CourseRetrieveModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

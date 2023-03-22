from rest_framework.viewsets import GenericViewSet

from django_filters import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import CourseDirection, CourseCategory, Course
from .serializers import CourseDirectionModelSerializer, CourseCategoryModelSerializer, CourseInfoModelSerializer

from mixins import ReListModelMixin


class CourseCategoryFilterSet(FilterSet):
    """
    获取方向下的全部分类
    http://127.0.0.1:8000/course/category/?direction=10
    """
    direction = filters.CharFilter(field_name='direction', label='课程分类名称')

    class Meta:
        model = CourseCategory
        fields = ('direction',)


class CourseDirectionGenericAPIView(GenericViewSet, ReListModelMixin):
    """学习方向"""
    queryset = CourseDirection.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseDirectionModelSerializer


class CourseCategoryGenericAPIView(GenericViewSet, ReListModelMixin):
    """课程分类"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CourseCategoryFilterSet

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
    """课程列表接口"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CourseInfoFilterSet

    queryset = Course.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseInfoModelSerializer

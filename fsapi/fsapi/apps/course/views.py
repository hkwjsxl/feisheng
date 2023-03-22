from rest_framework.viewsets import GenericViewSet

from .models import CourseDirection, CourseCategory
from .serializers import CourseDirectionModelSerializer, CourseCategoryModelSerializer

from mixins import ReListModelMixin


class CourseDirectionGenericAPIView(GenericViewSet, ReListModelMixin):
    """学习方向"""
    queryset = CourseDirection.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseDirectionModelSerializer


class CourseCategoryGenericAPIView(GenericViewSet, ReListModelMixin):
    """学习方向"""
    queryset = CourseCategory.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseCategoryModelSerializer

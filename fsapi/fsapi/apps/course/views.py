from rest_framework.viewsets import GenericViewSet

from .models import CourseDirection
from .serializers import CourseDirectionModelSerializer

from mixins import ReListModelMixin


class CourseDirectionGenericAPIView(GenericViewSet, ReListModelMixin):
    """学习方向"""
    queryset = CourseDirection.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = CourseDirectionModelSerializer

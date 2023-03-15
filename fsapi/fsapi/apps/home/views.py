from rest_framework.viewsets import GenericViewSet

from .models import Nav, Banner
from .serializers import NavModelSerializer, BannerModelSerializer
from mixins import ReListModelMixin
from constants import (
    NAV_HEADER_POSITION, NAV_FOOTER_POSITION, NAV_FOOTER_SIZE, NAV_HEADER_SIZE, BANNER_SIZE
)


class NavHeaderListAPIView(ReListModelMixin, GenericViewSet):
    """顶部导航视图"""
    queryset = Nav.objects.filter(
        position=NAV_HEADER_POSITION, is_show=True, is_deleted=False
    ).order_by("orders", "-id")[:NAV_HEADER_SIZE]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(ReListModelMixin, GenericViewSet):
    """脚部导航视图"""
    queryset = Nav.objects.filter(
        position=NAV_FOOTER_POSITION, is_show=True, is_deleted=False
    ).order_by("orders", "-id")[:NAV_FOOTER_SIZE]
    serializer_class = NavModelSerializer


class BannerListAPIView(ReListModelMixin, GenericViewSet):
    """轮播广告视图"""
    queryset = Banner.objects.filter(
        is_show=True, is_deleted=False
    ).order_by("orders", "-id")[:BANNER_SIZE]
    serializer_class = BannerModelSerializer

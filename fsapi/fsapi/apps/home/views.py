from .models import Nav, Banner
from .serializers import NavModelSerializer, BannerModelSerializer
from constants import (
    NAV_HEADER_POSITION, NAV_FOOTER_POSITION, NAV_FOOTER_SIZE, NAV_HEADER_SIZE, BANNER_SIZE
)
from views import CacheListAPIView


class NavHeaderListAPIView(CacheListAPIView):
    """顶部导航视图"""
    queryset = Nav.objects.filter(
        position=NAV_HEADER_POSITION, is_show=True, is_deleted=False
    ).order_by("orders", "-id")[:NAV_HEADER_SIZE]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(CacheListAPIView):
    """脚部导航视图"""
    queryset = Nav.objects.filter(
        position=NAV_FOOTER_POSITION, is_show=True, is_deleted=False
    ).order_by("orders", "-id")[:NAV_FOOTER_SIZE]
    serializer_class = NavModelSerializer


class BannerListAPIView(CacheListAPIView):
    """轮播广告视图"""
    queryset = Banner.objects.filter(
        is_show=True, is_deleted=False
    ).order_by("orders", "-id")[:BANNER_SIZE]
    serializer_class = BannerModelSerializer

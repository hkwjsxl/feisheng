from rest_framework import serializers
from .models import Nav, Banner


class NavModelSerializer(serializers.ModelSerializer):
    """
    导航菜单的序列化器
    """

    class Meta:
        model = Nav
        fields = ["name", "link", "is_http"]


class BannerModelSerializer(serializers.ModelSerializer):
    """
    轮播广告的序列化器
    """

    class Meta:
        model = Banner
        fields = ["name", "image", "link", "is_http"]

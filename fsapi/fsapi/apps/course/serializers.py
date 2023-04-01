from django.conf import settings

from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer

from .search_indexes import CourseIndex
from .models import CourseDirection, CourseCategory, Course


class CourseDirectionModelSerializer(serializers.ModelSerializer):
    """学习方向的序列化器"""

    class Meta:
        model = CourseDirection
        fields = ("id", "name")


class CourseCategoryModelSerializer(serializers.ModelSerializer):
    """课程分类的序列化器"""

    class Meta:
        model = CourseCategory
        fields = ("id", "name")


class CourseInfoModelSerializer(serializers.ModelSerializer):
    """课程信息的序列化器"""

    class Meta:
        model = Course
        fields = (
            "id", "name", "course_cover", "level", "get_level_display",
            "students", "status", "get_status_display",
            "lessons", "pub_lessons", "price", "discount"
        )


class CourseIndexHaystackSerializer(HaystackSerializer):
    """课程搜索的序列化器"""

    class Meta:
        index_classes = [CourseIndex]
        fields = ["text", "id", "name", "course_cover", "get_level_display", "students", "get_status_display",
                  "pub_lessons", "price", "discount", "orders"]

    def to_representation(self, instance):
        """用于指定返回数据的字段的"""
        # 课程的图片，在这里通过elasticsearch提供的，所以不会提供图片地址左边的域名的。因此在这里手动拼接
        # instance.course_cover = f'//{settings.OSS_BUCKET_NAME}.{settings.OSS_ENDPOINT}/uploads/{instance.course_cover}'
        instance.course_cover = f'/media/{instance.course_cover}'
        return super().to_representation(instance)

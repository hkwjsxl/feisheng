from django.conf import settings

from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer

from .search_indexes import CourseIndex
from .models import (
    CourseDirection, CourseCategory, Course, Teacher, CourseChapter
)


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
        instance.course_cover = f'{settings.BACKEND_URL}/media/{instance.course_cover}'
        return super().to_representation(instance)


class CourseTearchModelSerializer(serializers.ModelSerializer):
    """课程老师信息"""

    class Meta:
        model = Teacher
        fields = ["id", "name", "avatar", "role", "get_role_display", "title", "signature", "brief"]


class CourseRetrieveModelSerializer(serializers.ModelSerializer):
    """课程详情的序列化器"""
    direction_name = serializers.CharField(source="direction.name")
    # diretion = serializers.SlugRelatedField(read_only=True, slug_field='name')
    category_name = serializers.CharField(source="category.name")
    # 序列化器嵌套
    teacher = CourseTearchModelSerializer()

    class Meta:
        model = Course
        fields = [
            "name", "course_cover", "course_video", "level", "get_level_display",
            "description", "pub_date", "status", "get_status_display", "students", "discount",
            "lessons", "pub_lessons", "price", "direction",
            "direction_name", "category", "category_name",
            "teacher"
        ]


class CourseChapterModelSerializer(serializers.ModelSerializer):
    """课程章节序列化器"""

    class Meta:
        model = CourseChapter
        fields = ["id", "orders", "name", "summary", "get_lesson_list"]

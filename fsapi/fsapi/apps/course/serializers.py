from rest_framework import serializers

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

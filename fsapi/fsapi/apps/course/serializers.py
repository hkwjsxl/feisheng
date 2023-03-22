from rest_framework import serializers

from .models import CourseDirection, CourseCategory


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

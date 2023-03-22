from rest_framework import serializers

from .models import CourseDirection


class CourseDirectionModelSerializer(serializers.ModelSerializer):
    """学习方向的序列化器"""

    class Meta:
        model = CourseDirection
        fields = ("id", "name")

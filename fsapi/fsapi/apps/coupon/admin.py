import json

from django.contrib import admin
from django.utils import timezone as datetime

from django_redis import get_redis_connection

from .models import Coupon, CouponDirection, CouponCourseCat, CouponCourse, CouponLog
from logger import log
from coupon.services import add_coupon_to_redis


class CouponDirectionInLine(admin.TabularInline):  # admin.StackedInline
    """学习方向的内嵌类"""
    model = CouponDirection
    fields = ["id", "direction"]


class CouponCourseCatInLine(admin.TabularInline):  # admin.StackedInline
    """课程分类的内嵌类"""
    model = CouponCourseCat
    fields = ["id", "category"]


class CouponCourseInLine(admin.TabularInline):  # admin.StackedInline
    """课程信息的内嵌类"""
    model = CouponCourse
    fields = ["id", "course"]


class CouponModelAdmin(admin.ModelAdmin):
    """优惠券的模型管理器"""
    list_display = ["id", "name", "start_time", "end_time", "total", "has_total", "coupon_type", "get_type", ]
    inlines = [CouponDirectionInLine, CouponCourseCatInLine, CouponCourseInLine]


admin.site.register(Coupon, CouponModelAdmin)


class CouponLogModelAdmin(admin.ModelAdmin):
    """优惠券发放和使用日志"""
    list_display = ["id", "user", "coupon", "order", "use_time", "use_status"]

    def save_model(self, request, obj, form, change):
        """
        保存或更新记录时自动执行的钩子
        request: 本次客户端提交的请求对象
        obj: 本次操作的模型实例对象
        form: 本次客户端提交的表单数据
        change: 值为True，表示更新数据，值为False，表示添加数据
        """
        obj.save()

        # 同步记录到redis中
        redis = get_redis_connection("coupon")
        if obj.use_status == 0 and obj.use_time == None:
            # 未使用过的 记录优惠券信息到redis中
            add_coupon_to_redis(obj)
        else:
            # 使用过的优惠直接删除
            redis.delete(f"{obj.user.id}:{obj.id}")

    def delete_model(self, request, obj):
        """
        删除记录时自动执行的钩子
        详情页中删除一个记录时执行
        如果系统后台管理员删除当前优惠券记录，则redis中的对应记录也被删除
        """
        log.info(f"详情页中删除一个记录---{obj}")
        redis = get_redis_connection("coupon")
        redis.delete(f"{obj.user.id}:{obj.id}")
        obj.delete()

    def delete_queryset(self, request, queryset):
        """
        删除记录时自动执行的钩子
        列表页中删除多个记录时执行
        在列表页中进行删除优惠券记录时，也要同步删除容redis中的记录
        """
        log.info(f"列表页中删除多个记录---{queryset}")
        redis = get_redis_connection("coupon")
        for obj in queryset:
            redis.delete(f"{obj.user.id}:{obj.id}")
        queryset.delete()


admin.site.register(CouponLog, CouponLogModelAdmin)

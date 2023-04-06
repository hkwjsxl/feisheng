from django.contrib import admin
from .models import Coupon, CouponDirection, CouponCourseCat, CouponCourse, CouponLog


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


admin.site.register(CouponLog, CouponLogModelAdmin)

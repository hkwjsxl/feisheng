from django.apps import AppConfig


class CouponConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coupon'
    verbose_name = "优惠卷管理"
    verbose_name_plural = verbose_name

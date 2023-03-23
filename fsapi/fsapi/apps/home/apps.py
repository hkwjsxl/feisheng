from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    verbose_name = "公共数据"
    verbose_name_plural = verbose_name

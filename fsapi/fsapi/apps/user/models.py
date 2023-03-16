from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    money = models.DecimalField(max_digits=9, default=0.0, decimal_places=2, verbose_name="钱包余额")
    credit = models.IntegerField(default=0, verbose_name="积分")
    avatar = models.ImageField(upload_to="avatar/%Y", default="", null=True, blank=True, verbose_name="个人头像")
    nickname = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="用户昵称")

    class Meta:
        db_table = 'fs_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

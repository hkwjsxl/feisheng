from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe

from stdimage import StdImageField


class UserInfo(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    money = models.DecimalField(max_digits=9, default=0.0, decimal_places=2, verbose_name="钱包余额")
    credit = models.IntegerField(default=0, verbose_name="积分")
    avatar = StdImageField(
        variations={
            'thumb_800x800': (800, 800),
            'thumb_400x400': (400, 400),
            'thumb_50x50': (50, 50, True),
        }, delete_orphans=True, upload_to="avatar/%Y", default="avatar/2023/avatar.jpg",
        null=True, blank=True, verbose_name="个人头像"
    )
    nickname = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="用户昵称")

    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        db_table = 'fs_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "username---%s" % self.username

    def avatar_small(self):
        if self.avatar:
            return mark_safe(f'<img style="border-radius: 0%;" src="{self.avatar.thumb_50x50.url}">')
        return ""

    avatar_small.short_description = "用户头像(50x50)"
    avatar_small.allow_tags = True
    avatar_small.admin_order_field = "avatar"

    def avatar_medium(self):
        if self.avatar:
            return mark_safe(f'<img style="border-radius: 0%;" src="{self.avatar.thumb_400x400.url}">')
        return ""

    avatar_medium.short_description = "用户头像(400x400)"
    avatar_medium.allow_tags = True
    avatar_medium.admin_order_field = "avatar"

    def avatar_large(self):
        if self.avatar:
            return mark_safe(f'<img style="border-radius: 0%;" src="{self.avatar.thumb_800x800.url}">')
        return ""

    avatar_large.short_description = "用户头像(800x800)"
    avatar_large.allow_tags = True
    avatar_large.admin_order_field = "avatar"

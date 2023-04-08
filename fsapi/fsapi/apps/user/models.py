from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe

from stdimage import StdImageField

from models import BaseModel


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


class Credit(BaseModel):
    """积分流水"""
    opera_choices = (
        (0, "业务增值"),
        (1, "购物消费"),
        (2, "系统赠送"),
    )
    operation = models.SmallIntegerField(choices=opera_choices, default=1, verbose_name="积分操作类型")
    number = models.IntegerField(default=0, verbose_name="积分数量",
                                 help_text="如果是扣除积分则需要设置积分为负数，如果消费10积分，则填写-10，<br>如果是添加积分则需要设置积分为正数，如果获得10积分，则填写10。")
    user = models.ForeignKey(UserInfo, related_name='user_credits', on_delete=models.CASCADE, db_constraint=False,
                             verbose_name="用户")
    remark = models.CharField(max_length=500, null=True, blank=True, verbose_name="备注信息")

    class Meta:
        db_table = 'fs_credit'
        verbose_name = '积分流水'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.number > 0:
            oper_text = "获得"
        else:
            oper_text = "减少"

        return "[%s] %s 用户%s %s %s积分" % (
            self.get_operation_display(), self.created_time.strftime("%Y-%m-%d %H:%M:%S"), self.user.username,
            oper_text,
            abs(self.number)
        )

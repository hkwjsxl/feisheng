from django.db import models


class BaseModel(models.Model):
    """
    公共模型
    保存项目中的所有模型的公共属性和公共方法的声明
    """
    name = models.CharField(max_length=255, verbose_name="姓名/名称/标题")
    is_show = models.BooleanField(default=True, verbose_name="是否显示")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    orders = models.SmallIntegerField(default=0, verbose_name="序号")

    class Meta:
        # 不创建该表（抽象模型类）
        abstract = True

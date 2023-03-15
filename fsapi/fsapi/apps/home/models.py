from models import models, BaseModel


class Nav(BaseModel):
    """导航菜单"""
    POSITION_OPTION = (
        (0, "顶部导航"),
        (1, "脚部导航"),
    )
    link = models.CharField(max_length=255, verbose_name="导航链接")
    is_http = models.BooleanField(default=False, verbose_name="是否是外部链接")

    position = models.IntegerField(choices=POSITION_OPTION, default=0, verbose_name="导航位置")

    class Meta:
        db_table = "fs_nav"
        verbose_name = "导航菜单"
        verbose_name_plural = verbose_name

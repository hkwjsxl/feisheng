from models import BaseModel, models
from user.models import UserInfo
from course.models import Course


class Order(BaseModel):
    """订单基本信息模型"""
    status_choices = (
        (0, '未支付'),
        (1, '已支付'),
        (2, '已取消'),
        (3, '已超时'),
    )
    pay_choices = (
        (0, '支付宝'),
        (1, '微信'),
        (2, '余额'),
    )

    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="订单总价")
    real_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="实付金额")
    order_number = models.CharField(max_length=64, verbose_name="订单号")

    order_status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="订单状态")
    pay_type = models.SmallIntegerField(choices=pay_choices, default=0, verbose_name="支付方式")

    order_desc = models.TextField(null=True, blank=True, max_length=500, verbose_name="订单描述")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")

    user = models.ForeignKey(UserInfo, related_name='user_orders', on_delete=models.DO_NOTHING,
                             db_constraint=False, verbose_name="下单用户")

    credit = models.IntegerField(default=0, null=True, blank=True, verbose_name="积分")

    class Meta:
        db_table = "fs_order"
        verbose_name = "订单记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s,总价: %s,实付: %s" % (self.name, self.total_price, self.real_price)


class OrderDetail(BaseModel):
    """
    订单详情
    """
    order = models.ForeignKey(Order, related_name='order_courses', on_delete=models.CASCADE, db_constraint=False,
                              verbose_name="订单")
    course = models.ForeignKey(Course, related_name='course_orders', on_delete=models.CASCADE, db_constraint=False,
                               verbose_name="课程")

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="课程原价")
    real_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="课程实价")
    discount_name = models.CharField(max_length=120, default="", verbose_name="优惠类型")

    class Meta:
        db_table = "fs_order_course"
        verbose_name = "订单详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.course.name

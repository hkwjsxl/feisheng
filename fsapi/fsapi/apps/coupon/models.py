from models import BaseModel, models
from user.models import UserInfo
from orders.models import Order
from course.models import CourseDirection, CourseCategory, Course


class Coupon(BaseModel):
    discount_choices = (
        (1, '减免'),
        (2, '折扣'),
    )
    type_choices = (
        (0, '通用类型'),
        (1, '指定方向'),
        (2, '指定分类'),
        (3, '指定课程'),
    )
    get_choices = (
        (0, "系统赠送"),
        (1, "自行领取"),
    )
    discount = models.SmallIntegerField(choices=discount_choices, default=1, verbose_name="优惠方式")
    coupon_type = models.SmallIntegerField(choices=type_choices, default=0, verbose_name="优惠券类型")
    total = models.IntegerField(blank=True, default=100, verbose_name="发放数量")
    has_total = models.IntegerField(blank=True, default=100, verbose_name="剩余数量")
    start_time = models.DateTimeField(verbose_name="启用时间")
    end_time = models.DateTimeField(verbose_name="过期时间")
    get_type = models.SmallIntegerField(choices=get_choices, default=0, verbose_name="领取方式")
    condition = models.IntegerField(blank=True, default=0, verbose_name="满足使用优惠券的价格条件")
    per_limit = models.SmallIntegerField(default=1, verbose_name="每人限制领取数量")
    sale = models.TextField(verbose_name="优惠公式", help_text="""
            *号开头表示折扣价，例如*0.82表示八二折；<br>
            -号开头表示减免价,例如-10表示在总价基础上减免10元<br>   
            """)

    class Meta:
        db_table = "fs_coupon"
        verbose_name = "优惠券"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self)


class CouponDirection(models.Model):
    direction = models.ForeignKey(CourseDirection, on_delete=models.CASCADE, related_name="to_coupon",
                                  verbose_name="学习方向", db_constraint=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name="to_direction",
                               verbose_name="优惠券", db_constraint=False)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        db_table = "fs_coupon_course_direction"
        verbose_name = "优惠券与学习方向"
        verbose_name_plural = verbose_name


class CouponCourseCat(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name="to_coupon",
                                 verbose_name="课程分类", db_constraint=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name="to_category",
                               verbose_name="优惠券", db_constraint=False)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        db_table = "fs_coupon_course_category"
        verbose_name = "优惠券与课程分类"
        verbose_name_plural = verbose_name


class CouponCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="to_coupon",
                               verbose_name="课程", db_constraint=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name="to_course",
                               verbose_name="优惠券", db_constraint=False)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        db_table = "fs_coupon_course"
        verbose_name = "优惠券与课程信息"
        verbose_name_plural = verbose_name


class CouponLog(BaseModel):
    use_choices = (
        (0, "未使用"),
        (1, "已使用"),
        (2, "已过期"),
    )
    name = models.CharField(null=True, blank=True, max_length=100, verbose_name="名称/标题")

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="to_coupon",
                             verbose_name="用户", db_constraint=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name="to_user",
                               verbose_name="优惠券", db_constraint=False)
    order = models.ForeignKey(Order, null=True, blank=True, default=None, on_delete=models.CASCADE,
                              related_name="to_coupon", verbose_name="订单", db_constraint=False)

    use_time = models.DateTimeField(null=True, blank=True, verbose_name="使用时间")
    use_status = models.SmallIntegerField(choices=use_choices, null=True, blank=True, default=0,
                                          verbose_name="使用状态")

    class Meta:
        db_table = "fs_coupon_log"
        verbose_name = "优惠券发放和使用日志"
        verbose_name_plural = verbose_name

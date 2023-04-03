import json

from django.utils.safestring import mark_safe
from django.utils import timezone as datetime

from models import models, BaseModel

# 不支持上传文件
# from ckeditor.fields import RichTextField
# 支持上传文件
from ckeditor_uploader.fields import RichTextUploadingField
# 缩略图
from stdimage import StdImageField


class CourseDirection(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="方向名称")
    remark = RichTextUploadingField(default="", blank=True, null=True, verbose_name="方向描述")
    recomment_home_hot = models.BooleanField(default=False, verbose_name="是否推荐到首页新课栏目")
    recomment_home_top = models.BooleanField(default=False, verbose_name="是否推荐到首页必学栏目")

    class Meta:
        db_table = "fs_course_direction"
        verbose_name = "学习方向"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="分类名称")
    remark = RichTextUploadingField(default="", blank=True, null=True, verbose_name="分类描述")

    direction = models.ForeignKey(
        "CourseDirection",
        related_name="category_list", on_delete=models.DO_NOTHING,
        db_constraint=False, verbose_name="学习方向"
    )

    class Meta:
        db_table = "fs_course_category"
        verbose_name = "课程分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(BaseModel):
    course_type = (
        (0, '付费购买'),
        (1, '会员专享'),
        (2, '学位课程'),
    )
    level_choices = (
        (0, '初级'),
        (1, '中级'),
        (2, '高级'),
    )
    status_choices = (
        (0, '上线'),
        (1, '下线'),
        (2, '预上线'),
    )
    course_cover = StdImageField(variations={
        'thumb_1080x608': (1080, 608),  # 高清图
        'thumb_540x304': (540, 304),  # 中等比例,
        'thumb_108x61': (108, 61, True),  # 小图(第三个参数表示保持图片质量),
    }, max_length=255, delete_orphans=True, upload_to="course/cover", null=True, verbose_name="封面图片", blank=True)
    course_video = models.FileField(upload_to="course/video", max_length=255, verbose_name="封面视频",
                                    blank=True, null=True)

    course_type = models.SmallIntegerField(choices=course_type, default=0, verbose_name="付费类型")
    level = models.SmallIntegerField(choices=level_choices, default=1, verbose_name="难度等级")
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="课程状态")

    description = RichTextUploadingField(null=True, blank=True, verbose_name="详情介绍")
    pub_date = models.DateField(auto_now_add=True, verbose_name="发布日期")
    period = models.IntegerField(default=7, verbose_name="建议学习周期(day)")
    attachment_path = models.FileField(max_length=1000, blank=True, null=True, verbose_name="课件路径")
    attachment_link = models.CharField(max_length=1000, blank=True, null=True, verbose_name="课件链接")

    # 优化字段
    students = models.IntegerField(default=0, verbose_name="学习人数")
    lessons = models.IntegerField(default=0, verbose_name="总课时数量")
    pub_lessons = models.IntegerField(default=0, verbose_name="已更新课时数量")

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="课程原价", default=0)
    recomment_home_hot = models.BooleanField(default=False, verbose_name="是否推荐到首页新课栏目")
    recomment_home_top = models.BooleanField(default=False, verbose_name="是否推荐到首页必学栏目")

    direction = models.ForeignKey(
        "CourseDirection", related_name="course_list", on_delete=models.DO_NOTHING,
        null=True, blank=True, db_constraint=False, verbose_name="学习方向"
    )
    category = models.ForeignKey(
        "CourseCategory", related_name="course_list", on_delete=models.DO_NOTHING,
        null=True, blank=True, db_constraint=False, verbose_name="课程分类"
    )
    teacher = models.ForeignKey(
        "Teacher", related_name="course_list", on_delete=models.DO_NOTHING,
        null=True, blank=True, db_constraint=False, verbose_name="授课老师"
    )

    class Meta:
        db_table = "fs_course_info"
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name

    def course_cover_small(self):
        if self.course_cover:
            return mark_safe(f'<img style="border-radius: 0%;" src="{self.course_cover.thumb_108x61.url}">')
        return ""

    course_cover_small.short_description = "封面图片(108x61)"
    course_cover_small.allow_tags = True
    course_cover_small.admin_order_field = "course_cover"

    def course_cover_medium(self):
        if self.course_cover:
            return mark_safe(f'<img style="border-radius: 0%;" src="{self.course_cover.thumb_540x304.url}">')
        return ""

    course_cover_medium.short_description = "封面图片(540x304)"
    course_cover_medium.allow_tags = True
    course_cover_medium.admin_order_field = "course_cover"

    def course_cover_large(self):
        if self.course_cover:
            return mark_safe(f'<img style="border-radius: 0%;" src="{self.course_cover.thumb_1080x608.url}">')
        return ""

    course_cover_large.short_description = "封面图片(1080x608)"
    course_cover_large.allow_tags = True
    course_cover_large.admin_order_field = "course_cover"

    @property
    def discount(self):
        """通过计算获取当前课程的折扣优惠相关的信息"""
        # 获取折扣优惠相关的信息
        now_time = datetime.now()
        # 获取当前课程参与的最新活动记录
        # 活动__开始时间 < 当前时间 < 活动__结束时间
        last_activity_log = self.price_list.filter(
            activity__end_time__gt=now_time,
            activity__start_time__lt=now_time
        ).order_by("-id").first()

        type_text = ""  # 优惠类型的默认值
        price = -1  # 优惠价格
        expire = 0  # 优惠剩余时间

        if last_activity_log:
            # 获取优惠类型的提示文本
            type_text = last_activity_log.discount.discount_type.name

            # 获取限时活动剩余时间戳[单位：s]
            expire = last_activity_log.activity.end_time.timestamp() - now_time.timestamp()

            # 判断当前课程的价格是否满足优惠条件
            course_price = float(self.price)
            condition_price = float(last_activity_log.discount.condition)
            # 课程价格比优惠劵金额大时或相等时，加上优惠卷的优惠
            if course_price >= condition_price:
                # 计算本次课程参与了优惠以后的价格
                sale = last_activity_log.discount.sale
                if sale == "0":
                    # 免费
                    price = 0
                elif sale[0] == "*":
                    # 折扣
                    price = course_price * float(sale[1:])
                elif sale[0] == "-":
                    # 减免
                    price = course_price - float(sale[1:])
                price = float(f"{price:.2f}")

        data = {}
        if type_text:
            data["type"] = type_text
        if expire > 0:
            data["expire"] = expire
        if price != -1:
            data["price"] = price

        return data

    def discount_json(self):
        # 必须转成字符串才能保存到es中。所以该方法提供给es使用的。
        return json.dumps(self.discount)

    @property
    def can_free_study(self):
        """是否允许试学"""
        lesson_list = self.lesson_list.filter(is_deleted=False, is_show=True).order_by("orders").all()
        return len(lesson_list) > 0


class Teacher(BaseModel):
    role_choices = (
        (0, '讲师'),
        (1, '导师'),
        (2, '班主任'),
    )
    role = models.SmallIntegerField(choices=role_choices, default=0, verbose_name="讲师身份")
    title = models.CharField(max_length=64, verbose_name="职位、职称")
    signature = models.CharField(max_length=255, null=True, blank=True, verbose_name="导师签名")
    avatar = StdImageField(variations={
        'thumb_800x800': (800, 800),  # 'large': (800, 800),
        'thumb_400x400': (400, 400),  # 'medium': (400, 400),
        'thumb_50x50': (50, 50, True),  # 'small': (50, 50, True),
    }, delete_orphans=True, upload_to="teacher", null=True, blank=True, verbose_name="讲师头像")
    brief = RichTextUploadingField(max_length=1024, verbose_name="讲师描述")

    class Meta:
        db_table = "fs_teacher"
        verbose_name = "讲师信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name

    def avatar_small(self):
        if self.avatar:
            return mark_safe(f'<img style="border-radius: 100%;" src="{self.avatar.thumb_50x50.url}">')
        return ""

    avatar_small.short_description = "头像信息(50x50)"
    avatar_small.allow_tags = True
    avatar_small.admin_order_field = "avatar"

    def avatar_medium(self):
        if self.avatar:
            return mark_safe(f'<img style="border-radius: 100%;" src="{self.avatar.thumb_400x400.url}">')
        return ""

    avatar_medium.short_description = "头像信息(400x400)"
    avatar_medium.allow_tags = True
    avatar_medium.admin_order_field = "avatar"

    def avatar_large(self):
        if self.avatar:
            return mark_safe(f'<img style="border-radius: 100%;" src="{self.avatar.thumb_800x800.url}">')
        return ""

    avatar_large.short_description = "头像信息(800x800)"
    avatar_large.allow_tags = True
    avatar_large.admin_order_field = "avatar"


class CourseChapter(BaseModel):
    """课程章节"""
    orders = models.SmallIntegerField(default=1, verbose_name="第几章")
    summary = RichTextUploadingField(blank=True, null=True, verbose_name="章节介绍")
    pub_date = models.DateField(auto_now_add=True, verbose_name="发布日期")

    course = models.ForeignKey(
        "Course", related_name='chapter_list',
        on_delete=models.CASCADE, db_constraint=False, verbose_name="课程名称"
    )

    class Meta:
        db_table = "fs_course_chapter"
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-第%s章-%s" % (self.course.name, self.orders, self.name)

    def text(self):
        return self.__str__()

    # admin站点配置排序规则和显示的字段文本提示
    text.short_description = "章节名称"
    text.allow_tags = True
    text.admin_order_field = "orders"

    def get_lesson_list(self):
        """返回当前章节的课时列表"""
        lesson_list = self.lesson_list.filter(is_deleted=False, is_show=True).order_by("orders").all()
        return [{
            "id": lesson.id,
            "name": lesson.name,
            "orders": lesson.orders,
            "duration": lesson.duration,
            "lesson_type": lesson.lesson_type,
            "lesson_link": lesson.lesson_link,
            "free_trail": lesson.free_trail
        } for lesson in lesson_list]


class CourseLesson(BaseModel):
    """课程课时"""
    lesson_type_choices = (
        (0, '文档'),
        (1, '练习'),
        (2, '视频'),
    )
    orders = models.SmallIntegerField(default=1, verbose_name="第几节")
    lesson_type = models.SmallIntegerField(default=2, choices=lesson_type_choices, verbose_name="课时种类")
    lesson_link = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="若是video，填视频地址或者视频id，若是文档，填文档地址", verbose_name="课时链接"
    )
    duration = models.CharField(blank=True, null=True, max_length=32, verbose_name="课时时长")  # 仅在前端展示使用
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    free_trail = models.BooleanField(default=False, verbose_name="是否可试看")
    recomment = models.BooleanField(default=False, verbose_name="是否推荐到课程列表")

    chapter = models.ForeignKey(
        "CourseChapter", related_name='lesson_list', on_delete=models.CASCADE,
        db_constraint=False, verbose_name="章节"
    )
    course = models.ForeignKey(
        "Course", related_name="lesson_list", on_delete=models.DO_NOTHING,
        db_constraint=False, verbose_name="课程"
    )

    class Meta:
        db_table = "fs_course_lesson"
        verbose_name = "课程课时"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.chapter, self.name)

    def text(self, obj):
        return obj.__str__()

    # admin站点配置排序规则和显示的字段文本提示
    text.short_description = "课时名称"
    text.allow_tags = True
    text.admin_order_field = "orders"


class Activity(BaseModel):
    name = models.CharField(max_length=255, verbose_name="活动名称")
    start_time = models.DateTimeField(default=datetime.now, verbose_name="开始时间")
    end_time = models.DateTimeField(default=datetime.now, verbose_name="结束时间")
    description = RichTextUploadingField(blank=True, null=True, verbose_name="活动介绍")
    remark = models.TextField(blank=True, null=True, verbose_name="备注信息")

    class Meta:
        db_table = "fs_activity"
        verbose_name = "优惠活动"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class DiscountType(BaseModel):
    remark = models.CharField(max_length=255, blank=True, null=True, verbose_name="备注信息")

    class Meta:
        db_table = "fs_discount_type"
        verbose_name = "优惠类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Discount(BaseModel):
    discount_type = models.ForeignKey("DiscountType", on_delete=models.CASCADE, related_name='discount_list',
                                      db_constraint=False, verbose_name="优惠类型")
    # 要优惠的价格
    condition = models.IntegerField(blank=True, default=0, verbose_name="满足优惠的价格条件",
                                    help_text="设置享受优惠的价格条件,如果不填或0则没有优惠门槛")
    sale = models.TextField(
        verbose_name="优惠公式", help_text="""
        0表示免费；<br>
        *号开头表示折扣价，例如填写*0.82,则表示八二折；<br>
        -号开头表示减免价, 例如填写-100,则表示减免100；<br>"""
    )

    class Meta:
        db_table = "fs_discount"
        verbose_name = "优惠公式"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "价格优惠:%s,优惠条件:%s,优惠公式: %s" % (self.discount_type.name, self.condition, self.sale)


class CourseActivityPrice(BaseModel):
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE, related_name='price_list',
                                 db_constraint=False, verbose_name="活动")
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name='price_list',
                               db_constraint=False, verbose_name="课程")
    discount = models.ForeignKey("Discount", on_delete=models.CASCADE, related_name='price_list',
                                 db_constraint=False, verbose_name="优惠")

    class Meta:
        db_table = "fs_course_activity_price"
        verbose_name = "课程参与活动的价格表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "活动:%s-课程:%s-优惠公式:%s" % (self.activity.name, self.course.name, self.discount.sale)

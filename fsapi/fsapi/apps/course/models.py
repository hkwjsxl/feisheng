from models import models, BaseModel


class CourseDirection(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="方向名称")
    remark = models.TextField(default="", blank=True, null=True, verbose_name="方向描述")
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
    remark = models.TextField(default="", blank=True, null=True, verbose_name="分类描述")

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
    course_cover = models.ImageField(upload_to="course/cover", max_length=255, verbose_name="封面图片",
                                     blank=True, null=True)
    course_video = models.FileField(upload_to="course/video", max_length=255, verbose_name="封面视频",
                                    blank=True, null=True)

    course_type = models.SmallIntegerField(choices=course_type, default=0, verbose_name="付费类型")
    level = models.SmallIntegerField(choices=level_choices, default=1, verbose_name="难度等级")
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="课程状态")

    description = models.TextField(null=True, blank=True, verbose_name="详情介绍")
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


class Teacher(BaseModel):
    role_choices = (
        (0, '讲师'),
        (1, '导师'),
        (2, '班主任'),
    )
    role = models.SmallIntegerField(choices=role_choices, default=0, verbose_name="讲师身份")
    title = models.CharField(max_length=64, verbose_name="职位、职称")
    signature = models.CharField(max_length=255, null=True, blank=True, verbose_name="导师签名")
    avatar = models.ImageField(upload_to="teacher", null=True, blank=True, verbose_name="讲师头像")
    brief = models.TextField(max_length=1024, verbose_name="讲师描述")

    class Meta:
        db_table = "fs_teacher"
        verbose_name = "讲师信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class CourseChapter(BaseModel):
    """课程章节"""
    orders = models.SmallIntegerField(default=1, verbose_name="第几章")
    summary = models.TextField(blank=True, null=True, verbose_name="章节介绍")
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

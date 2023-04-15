from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe

from stdimage import StdImageField
from ckeditor_uploader.fields import RichTextUploadingField  # 支持上传文件

from models import BaseModel
from course.models import Course, CourseChapter, CourseLesson


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
    study_time = models.IntegerField(default=0, verbose_name="总学习时长")

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


class UserCourse(BaseModel):
    """用户的课程"""
    user = models.ForeignKey(UserInfo, related_name='user_courses', on_delete=models.CASCADE,
                             verbose_name="用户", db_constraint=False)
    course = models.ForeignKey(Course, related_name='course_users', on_delete=models.CASCADE,
                               verbose_name="课程名称", db_constraint=False)
    chapter = models.ForeignKey(CourseChapter, related_name="user_chapter", on_delete=models.DO_NOTHING,
                                null=True, blank=True, verbose_name="章节信息", db_constraint=False)
    lesson = models.ForeignKey(CourseLesson, related_name="user_lesson", on_delete=models.DO_NOTHING,
                               null=True, blank=True, verbose_name="课时信息", db_constraint=False)

    study_time = models.IntegerField(default=0, verbose_name="学习时长")

    class Meta:
        db_table = 'fs_user_course'
        verbose_name = '用户课程购买记录'
        verbose_name_plural = verbose_name

    def progress(self):
        """学习进度值"""
        # 获取当前课程学习的最后一个章节
        if not self.chapter:
            return 0

        # 获取当前课程的总章数
        chapter_total = self.course.chapter_list.count()
        if chapter_total < 1:
            return 0

        # 获取当前已经完成学习的章节的序号
        chapter_order = self.chapter.orders - 1
        # 获取章节学习进度
        chapter_progress = float(f"{((chapter_order / chapter_total) * 100):.2f}")

        # 获取当前最后学习章节的总课时
        lesson_total = self.chapter.lesson_list.count()
        if lesson_total < 1:
            return 0

        # 获取当前已经完成学习的课时的序号
        lesson_order = self.lesson.orders - 1
        # 获取课时学习进度
        lesson_progress = float(f"{((lesson_order / lesson_total) * 100):.2f}")
        # 总学习进度 = 章节学习进度 + (100 / 总章数) * 课时学习进度
        # 总学习进度 = 章节学习进度 + 单章学习进度 * 课时学习进度
        course_progress = chapter_progress + (100 / chapter_total) * lesson_progress / 100

        return f"{course_progress:.2f}"

    def note(self):
        """笔记数量"""
        return 0

    def qa(self):
        """问答数量"""
        return 0

    def code(self):
        """代码数量"""
        return 0


class StudyProgress(models.Model):
    user = models.ForeignKey(UserInfo, related_name='to_progress', on_delete=models.CASCADE, verbose_name="用户",
                             db_constraint=False)
    lesson = models.ForeignKey(CourseLesson, related_name="to_progress", on_delete=models.DO_NOTHING, null=True,
                               blank=True, verbose_name="课时信息", db_constraint=False)
    study_time = models.IntegerField(default=0, verbose_name="学习时长")

    class Meta:
        db_table = 'fs_study_progress'
        verbose_name = '课时进度记录'
        verbose_name_plural = verbose_name


class StudyCode(models.Model):
    user = models.ForeignKey(UserInfo, related_name='to_code', on_delete=models.CASCADE, verbose_name="用户",
                             db_constraint=False)
    course = models.ForeignKey(Course, related_name='to_code', on_delete=models.CASCADE, verbose_name="课程名称",
                               db_constraint=False)
    chapter = models.ForeignKey(CourseChapter, related_name="to_code", on_delete=models.DO_NOTHING, null=True,
                                blank=True, verbose_name="章节信息", db_constraint=False)
    lesson = models.ForeignKey(CourseLesson, related_name="to_code", on_delete=models.DO_NOTHING, null=True, blank=True,
                               verbose_name="课时信息", db_constraint=False)
    code = RichTextUploadingField(default="", blank="", verbose_name="练习代码")

    class Meta:
        db_table = 'fs_study_code'
        verbose_name = '代码记录'
        verbose_name_plural = verbose_name


class StudyQA(models.Model):
    user = models.ForeignKey(UserInfo, related_name='to_qa', on_delete=models.CASCADE, verbose_name="用户",
                             db_constraint=False)
    course = models.ForeignKey(Course, related_name='to_qa', on_delete=models.CASCADE, verbose_name="课程名称",
                               db_constraint=False)
    chapter = models.ForeignKey(CourseChapter, related_name="to_qa", on_delete=models.DO_NOTHING, null=True, blank=True,
                                verbose_name="章节信息", db_constraint=False)
    lesson = models.ForeignKey(CourseLesson, related_name="to_qa", on_delete=models.DO_NOTHING, null=True, blank=True,
                               verbose_name="课时信息", db_constraint=False)
    question = RichTextUploadingField(default="", blank="", verbose_name="问题")
    answer = RichTextUploadingField(default="", blank="", verbose_name="回答")

    class Meta:
        db_table = 'fs_study_qa'
        verbose_name = '问答记录'
        verbose_name_plural = verbose_name


class StudyNote(BaseModel):
    user = models.ForeignKey(UserInfo, related_name='to_note', on_delete=models.CASCADE, verbose_name="用户",
                             db_constraint=False)
    course = models.ForeignKey(Course, related_name='to_note', on_delete=models.CASCADE, verbose_name="课程名称",
                               db_constraint=False)
    chapter = models.ForeignKey(CourseChapter, related_name="to_note", on_delete=models.DO_NOTHING, null=True,
                                blank=True, verbose_name="章节信息", db_constraint=False)
    lesson = models.ForeignKey(CourseLesson, related_name="to_note", on_delete=models.DO_NOTHING, null=True, blank=True,
                               verbose_name="课时信息", db_constraint=False)
    content = RichTextUploadingField(default="", blank="", verbose_name="笔记内容")

    class Meta:
        db_table = 'fs_study_note'
        verbose_name = '学习笔记'
        verbose_name_plural = verbose_name

from django.core.management.base import BaseCommand, CommandError
from course.models import Teacher


# 类名必须是Command而且一个文件就是一个命令类，这个命令类必须直接或间接继承BaseCommand
class Command(BaseCommand):
    help = '添加课程相关的测试数据'

    # 如果当前命令，需要接受来自终端的参数，可以使用add_arguments
    def add_arguments(self, parser):
        pass
        # 位置参数，必填项
        # parser.add_argument('name', nargs='+', type=int)

        # 命令参数，可选项
        # parser.add_argument(
        #     '--table',
        #     action='store_true',
        #     help='Delete poll instead of closing it',
        # )

    # 命令执行的核心方法，
    def handle(self, *args, **options):
        """添加测试数据"""
        print("添加测试数据")

        Teacher.objects.create(
            name="赵小明",
            avatar="teacher/avatar.jpg",
            role=1,
            title="老师",
            signature="从业3年，管理班级无数",
            brief="从业3年，管理班级无数",
        )

# python manage.py example

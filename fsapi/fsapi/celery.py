import os
from celery import Celery

# 必须在实例化celery应用对象之前执行
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fsapi.settings.dev')

# 实例化celery应用对象
app = Celery('fsapi')
# 指定任务的队列名称
app.conf.task_default_queue = 'Celery'
# 也可以把配置写在django的项目配置中
# 设置django中配置信息以 "CELERY_"开头为celery的配置信息
app.config_from_object('django.conf:settings', namespace='CELERY')
# 自动根据配置查找django的所有子应用下的tasks任务文件
app.autodiscover_tasks()

# 启动
# celery -A fsapi worker -l info
# celery -A fsapi beat
# windows如果可以运行celery但没有执行任务，可以用下面的命令
# celery -A fsapi worker --pool=solo -l info

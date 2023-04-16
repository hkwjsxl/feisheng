import os

from django.conf import settings
# admin站点公共配置
from django.contrib import admin

# 服务器ip
SERVER_IP = "47.120.38.34"

# mysql相关
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_HOST = SERVER_IP
MYSQL_PORT = 3306
# redis相关
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_HOST = SERVER_IP
REDIS_PORT = 6379
# 容联云短信
RONGLIANYUN = {
    "accId": '2c94811c86c00e9b0186f2873a040afa',
    "accToken": os.environ.get("RONGLIANYUNACCTOKEN"),
    "appId": '2c94811c86c00e9b0186f2873b0d0b01',
    "reg_tid": 1,  # 注册短信验证码的模板ID
    "sms_expire": 60,  # 短信有效期，单位：秒(s)
    "sms_interval": 60,  # 短信发送的冷却时间，单位：秒(s)
}

# 用户默认头像
DEFAULT_USER_AVATAR = "avatar/2023/avatar.jpg"

"""
celery相关配置
"""
# Celery异步任务队列框架的配置项[注意：django的配置项必须大写，所以这里的所有配置项必须全部大写]
# 任务队列
CELERY_BROKER_URL = 'redis://:%s@%s:%s/14' % (
    REDIS_PASSWORD, REDIS_HOST, REDIS_PORT
)
# 结果队列
CELERY_RESULT_BACKEND = 'redis://:%s@%s:%s/15' % (
    REDIS_PASSWORD, REDIS_HOST, REDIS_PORT
)
# 时区，与django的时区同步
CELERY_TIMEZONE = settings.TIME_ZONE
# 防止死锁
CELERY_FORCE_EXECV = True
# 设置并发的worker数量
CELERYD_CONCURRENCY = 200
# celery的任务结果内容格式
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
# 设置失败允许重试[这个慎用，如果失败任务无法再次执行成功，会产生指数级别的失败记录]
# CELERY_ACKS_LATE = True
# 每个worker工作进程最多执行500个任务被销毁，可以防止内存泄漏，500是举例，根据自己的服务器的性能可以调整数值
# CELERYD_MAX_TASKS_PER_CHILD = 500
# 单个任务的最大运行时间，超时会被杀死[慎用，有大文件操作、长时间上传、下载任务时，需要关闭这个选项，或者设置更长时间]
# CELERYD_TIME_LIMIT = 10 * 60
# 任务发出后，经过一段时间还未收到acknowledge, 就将任务重新交给其他worker执行
CELERY_DISABLE_RATE_LIMITS = True

# 之前定时任务（定时一次调用），使用了apply_async({}, countdown=30);
# 设置定时任务（定时多次调用）的调用列表，需要单独运行SCHEDULE命令才能让celery执行定时任务：
# celery -A celeryapp.main beat，当然worker还是要启动的
# https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html

# from celery.schedules import crontab
# CELERY_BEAT_SCHEDULE = {
#     "send_sms1": {  # 定时任务的注册标记符[必须唯一的]
#         "task": "send_sms1",  # 定时任务的任务名称
#         "schedule": 10,  # 定时任务的调用时间，10表示每隔10秒调用一次add任务
#         # "schedule": crontab(hour=7, minute=30, day_of_week=1),  # 定时任务的调用时间，每周一早上7点30分调用一次add任务
#     }
# }


admin.AdminSite.site_header = '飞升在线'
admin.AdminSite.site_title = '飞升在线教育站点管理'

# 登录界面logo
SIMPLEUI_LOGO = '/media/backends/logo.png'
# 快速操作
SIMPLEUI_HOME_QUICK = True
# 服务器信息
SIMPLEUI_HOME_INFO = True

# 关闭simpleui内置的使用分析
SIMPLEUI_ANALYSIS = False
# 离线模式
SIMPLEUI_STATIC_OFFLINE = True
# 首页图标地址
SIMPLEUI_INDEX = 'http://www.fs.hkwpro.com/'

# 后台访问地址
BACKEND_URL = "http://api.fs.hkwpro.com:8000"
# 前端访问地址
FRONT_END_URL = 'http://www.fs.hkwpro.com'

# 保利威视频加密服务
POLYV = {
    "userId": "085a2e302a",
    "writeToken": "a1765fbd-19e4-48a9-8386-4a5802107842",
    "readToken": "12e97ba9-1c84-43b1-ba63-962cbad5824a",
    "secretkey": "yi10YtdCHd",
    "tokenUrl": "https://hls.videocc.net/service/v1/token",
}

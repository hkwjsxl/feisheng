from celery import Celery

# 实例化celery应用，参数一般为项目应用名
app = Celery("fsapi")

# 通过app实例对象加载配置文件
app.config_from_object("celeryapp.settings")

# 注册任务， 自动搜索并加载任务
# 参数必须必须是一个列表，里面的每一个任务都是任务的路径名称
# app.autodiscover_tasks(["任务1","任务2",....])
app.autodiscover_tasks(["celeryapp.sms"])

# 启动Celery的终端命令
# 强烈建议切换目录到项目的根目录下启动celery!!
# celery -A celeryapp.main worker --loglevel=info

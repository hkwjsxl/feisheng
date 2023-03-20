import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fsapi.settings.dev')
django.setup()
from django.conf import settings

# 任务队列的链接地址
broker_url = 'redis://:%s@%s:%s/14' % (
    settings.REDIS_PASSWORD, settings.REDIS_HOST, settings.REDIS_PORT
)
# 结果队列的链接地址
result_backend = 'redis://:%s@%s:%s/15' % (
    settings.REDIS_PASSWORD, settings.REDIS_HOST, settings.REDIS_PORT
)

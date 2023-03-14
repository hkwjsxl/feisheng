import os

# mysql相关
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
# redis相关
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379

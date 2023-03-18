import os

# mysql相关
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
# redis相关
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_HOST = "127.0.0.1"
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

from celery import shared_task

from logger import log
from sms.ronglianyunapi import send_sms as start_send_sms


@shared_task(name="send_sms")
def send_sms(tid, mobile, datas):
    """异步发送短信"""
    try:
        return start_send_sms(tid, mobile, datas)
    except Exception as e:
        log.error(f"手机号：{mobile}，发送短信失败错误: {e}")


# @shared_task(name="send_sms1")
# def send_sms1():
#     print("send_sms1执行了！！！")

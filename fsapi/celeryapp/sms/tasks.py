from ..main import app

from sms.ronglianyunapi import send_sms as start_send_sms


@app.task(name="send_sms")
def send_sms(tid, mobile, datas):
    return start_send_sms(tid, mobile, datas)

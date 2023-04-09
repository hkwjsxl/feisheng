from django.conf import settings

from alipay import AliPay
from alipay.utils import AliPayConfig

# 读取支付宝公钥与商户私钥
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
%s
-----END RSA PRIVATE KEY-----""" % open(settings.ALIPAY["app_private_key_path"]).read()

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
%s
-----END PUBLIC KEY-----""" % open(settings.ALIPAY["alipay_public_key_path"]).read()

alipay = AliPay(
    appid=settings.ALIPAY["appid"],
    app_notify_url=settings.ALIPAY["notify_url"],  # 默认回调 url
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=alipay_public_key_string,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
    sign_type=settings.ALIPAY["sign_type"],
    debug=settings.ALIPAY["debug"],  # 默认 False，沙箱模式下必须设置为True
    verbose=settings.ALIPAY["verbose"],  # 输出调试数据
    config=AliPayConfig(timeout=settings.ALIPAY["timeout"])  # 可选，请求超时时间，单位：秒
)

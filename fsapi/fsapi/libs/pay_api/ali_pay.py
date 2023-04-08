from django.conf import settings

from .client import alipay


def pay(out_trade_no, total_amount, subject):
    # 电脑网站支付，需要跳转到：https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=out_trade_no,  # 订单号
        total_amount=total_amount,  # 订单金额 单位：元
        subject=subject,  # 订单标题
        return_url=settings.ALIPAY["return_url"],  # 可选，同步回调地址，必须填写客户端的路径
        notify_url=settings.ALIPAY["notify_url"]  # 可选，不填则使用采用全局默认notify_url，必须填写服务端的路径
    )
    pay_url = '%s?%s' % (settings.ALIPAY['gateway'], order_string)
    return pay_url

    # order_string = alipay.client_api(
    #     "alipay.trade.page.pay",  # 接口名称
    #     biz_content={
    #         "out_trade_no": out_trade_no,  # 订单号
    #         "total_amount": total_amount,  # 订单金额 单位：元
    #         "subject": subject,  # 订单标题
    #         "product_code": "FAST_INSTANT_TRADE_PAY",  # 产品码，目前只能支持 FAST_INSTANT_TRADE_PAY
    #     },
    #     return_url=settings.ALIPAY["return_url"],  # 可选，同步回调地址，必须填写客户端的路径
    #     notify_url=settings.ALIPAY["notify_url"]  # 可选，不填则使用采用全局默认notify_url，必须填写服务端的路径
    # )
    #
    # # 拼接完整的支付链接
    # link = f"{settings.ALIPAY['gateway']}?{order_string}"
    # return link

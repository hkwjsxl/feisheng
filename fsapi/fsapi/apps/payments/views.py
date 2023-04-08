from rest_framework.viewsets import ViewSet

from orders.models import Order

from response import APIResponse
from pay_api.ali_pay import pay


class AlipayAPIViewSet(ViewSet):
    """支付宝接口"""

    def link(self, request, order_number):
        """生成支付宝支付链接信息"""
        try:
            order = Order.objects.get(order_number=order_number)
            if order.order_status > 0:
                return APIResponse(message="对不起，当前订单不能重复支付或订单已超时.")
        except Order.DoesNotExist:
            return APIResponse(message="对不起，当前订单不存在.")

        link = pay(order_number, float(order.real_price), order.name)

        return APIResponse(data={
            "pay_type": 0,  # 支付类型
            "get_pay_type_display": "支付宝",  # 支付类型的提示
            "link": link  # 支付连接地址
        })

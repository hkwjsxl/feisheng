from celery import shared_task
from django.db import transaction
from .models import Order
from coupon.services import add_coupon_to_redis

from logger import log


@shared_task(name="order_timeout")
def order_timeout(order_id):
    print(f"要超时取消的订单ID={order_id}")
    try:
        order = Order.objects.get(pk=order_id)
    except Exception as e:
        log.warning(f"订单不存在！order_id:{order_id}: {e}")
        return

    if order.order_status == 0:
        """只针对未支付的订单进行超时取消"""
        with transaction.atomic():
            save_id = transaction.savepoint()
            try:
                # 1. 查询当前订单是否使用了积分，如果有则恢复
                if order.credit > 0:
                    order.user.credit += order.credit
                    order.user.save()

                # 2. 查询当前订单是否使用了优惠券，如果有则恢复
                obj = order.to_coupon.first()
                if obj:
                    add_coupon_to_redis(obj)

                # 3. 切换当前订单为取消状态
                order.order_status = 3
                order.save()

                return {"order_id": order.id, "status": True, "errmsg": f"订单超时取消成功！"}

            except Exception as e:
                transaction.savepoint_rollback(save_id)
                log.warning(f"过期订单无法处理！order_id:{order_id}: {e}")
                return {"order_id": order.id, "status": False, "errmsg": f"{e}"}

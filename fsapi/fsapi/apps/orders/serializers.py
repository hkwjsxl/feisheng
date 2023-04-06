from datetime import datetime

from django.db import transaction

from rest_framework import serializers
from rest_framework import exceptions
from django_redis import get_redis_connection

from .models import Order, OrderDetail, Course

from logger import log


class OrderModelSerializer(serializers.ModelSerializer):
    pay_link = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ["pay_type", "id", "order_number", "pay_link"]
        read_only_fields = ["id", "order_number"]
        extra_kwargs = {
            "pay_type": {"write_only": True},
        }

    def create(self, validated_data):
        """创建订单"""
        redis = get_redis_connection("cart")
        user_id = self.context["request"].user.id
        with transaction.atomic():
            # 设置事务回滚的标记点,一个事物中可以设置多个回滚标记
            transaction_start = transaction.savepoint()
            try:
                # 创建订单记录
                order = Order.objects.create(
                    name="购买课程",  # 订单标题
                    user_id=user_id,  # 当前下单的用户ID
                    # order_number = datetime.now().strftime("%Y%m%d%H%M%S") + ("%08d" % user_id) + "%08d" % random.randint(1,99999999) # 基于随机数生成唯一订单号
                    order_number=datetime.now().strftime("%Y%m%d") + ("%08d" % user_id) + "%08d" % redis.incr(
                        "order_number"),
                    # 基于redis生成分布式唯一订单号
                    pay_type=validated_data.get("pay_type"),  # 支付方式
                )

                # 记录本次下单的商品列表
                cart_hash = redis.hgetall(f"cart_{user_id}")
                if len(cart_hash) < 1:
                    raise serializers.ValidationError(detail="购物车没有要下单的商品")

                # 提取购物车中所有勾选状态为b'1'的商品
                course_id_list = [int(key.decode()) for key, value in cart_hash.items() if value == b'1']

                # 添加订单与课程的关系
                course_list = Course.objects.filter(pk__in=course_id_list, is_deleted=False, is_show=True).all()
                detail_list = []
                total_price = 0  # 本次订单的总价格
                real_price = 0  # 本次订单的实付总价

                for course in course_list:
                    discount_price = float(course.discount.get("price", 0))  # 获取课程原价
                    discount_name = course.discount.get("type", "")
                    detail_list.append(OrderDetail(
                        order=order,
                        course=course,
                        name=course.name,
                        price=course.price,
                        real_price=discount_price,
                        discount_name=discount_name,
                    ))

                    # 统计订单的总价和实付总价
                    total_price += float(course.price)
                    real_price += discount_price if discount_price > 0 else float(course.price)

                # 一次性批量添加本次下单的商品记录
                OrderDetail.objects.bulk_create(detail_list)

                # 保存订单的总价格和实付价格
                order.total_price = total_price
                order.real_price = real_price
                order.save()

                # todo 支付链接地址[后面实现支付功能的时候，再做]
                order.pay_link = ""

                # 删除购物车中被勾选的商品，保留没有被勾选的商品信息
                cart_no_selectd = {key: value for key, value in cart_hash.items() if value == b'0'}
                pipe = redis.pipeline()
                pipe.multi()
                # 删除原来的购物车
                pipe.delete(f"cart_{user_id}")
                # 重新把未勾选的商品记录到购物车中
                pipe.hset(f"cart_{user_id}", cart_no_selectd)
                # hset 在新版本的redis中实际上hmset已经被废弃了，改用hset替代hmset
                pipe.execute()

                return order

            except Exception as e:
                log.error(f"订单创建失败：{e}")
                transaction.savepoint_rollback(transaction_start)
                raise exceptions.ValidationError(detail="订单创建失败.")

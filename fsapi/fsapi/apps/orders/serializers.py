from datetime import datetime

from django.db import transaction

from rest_framework import serializers
from rest_framework import exceptions
from django_redis import get_redis_connection

from .models import Order, OrderDetail, Course
from coupon.models import CouponLog

from logger import log


class OrderModelSerializer(serializers.ModelSerializer):
    pay_link = serializers.CharField(read_only=True)
    user_coupon_id = serializers.IntegerField(write_only=True, default=-1)

    class Meta:
        model = Order
        fields = ["pay_type", "id", "order_number", "pay_link", "user_coupon_id"]
        read_only_fields = ["id", "order_number"]
        extra_kwargs = {
            "pay_type": {
                "write_only": True,
            },
        }

    def create(self, validated_data):
        """创建订单"""
        redis = get_redis_connection("cart")
        user_id = self.context["request"].user.id

        # 判断用户如果使用了优惠券，则优惠券需要判断验证
        user_coupon_id = validated_data.get("user_coupon_id")
        # 本次下单时，用户使用的优惠券
        user_coupon = None
        if user_coupon_id != -1:
            user_coupon = CouponLog.objects.filter(pk=user_coupon_id, user_id=user_id).first()

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
                    pay_type=validated_data.get("pay_type", 0),  # 支付方式,默认是支付宝支付
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

                # 用户使用优惠券或积分以后，需要在服务端计算本次使用优惠券或积分的最大优惠额度
                total_discount_price = 0  # 总优惠价格
                max_discount_course = None  # 享受最大优惠的课程

                for course in course_list:
                    discount_price = course.discount.get("price", None)  # 获取课程原价
                    if discount_price is not None:
                        discount_price = float(discount_price)
                    discount_name = course.discount.get("type", "")
                    detail_list.append(OrderDetail(
                        order=order,
                        course=course,
                        name=course.name,
                        price=course.price,
                        real_price=course.price if discount_price is None else discount_price,
                        discount_name=discount_name,
                    ))

                    # 统计订单的总价和实付总价
                    total_price += float(course.price)
                    real_price += float(course.price if discount_price is None else discount_price)

                    # 在用户使用了优惠券，并且当前课程没有参与其他优惠活动时，找到最佳优惠课程
                    if user_coupon and discount_price is None:
                        if max_discount_course is None:
                            max_discount_course = course
                        else:
                            if course.price >= max_discount_course.price:
                                max_discount_course = course

                # 在用户使用了优惠券以后，根据循环中得到的最佳优惠课程进行计算最终抵扣金额
                if user_coupon:
                    # 优惠公式
                    sale = float(user_coupon.coupon.sale[1:])
                    if user_coupon.coupon.discount == 1:
                        """减免优惠券"""
                        total_discount_price = sale
                    elif user_coupon.coupon.discount == 2:
                        """折扣优惠券"""
                        total_discount_price = float(max_discount_course.price) * (1 - sale)

                # 一次性批量添加本次下单的商品记录
                OrderDetail.objects.bulk_create(detail_list)

                # 保存订单的总价格和实付价格
                order.total_price = total_price
                order.real_price = float(real_price - total_discount_price)
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
                # hmset不能设置空值
                if cart_no_selectd:
                    pipe.hmset(f"cart_{user_id}", cart_no_selectd)
                # hset 在新版本的redis中实际上hmset已经被废弃了，改用hset替代hmset
                pipe.execute()

                # 如果有使用了优惠券，则把优惠券和当前订单进行绑定
                if user_coupon:
                    user_coupon.order = order
                    user_coupon.save()
                    # 把优惠券从redis中移除
                    redis = get_redis_connection("coupon")
                    redis.delete(f"{user_id}:{user_coupon_id}")

                return order

            except Exception as e:
                log.error(f"订单创建失败：{e}")
                transaction.savepoint_rollback(transaction_start)
                raise exceptions.ValidationError("订单创建失败.")

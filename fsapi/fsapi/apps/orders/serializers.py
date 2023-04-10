from datetime import datetime

from django.db import transaction

from rest_framework import serializers
from rest_framework import exceptions
from django_redis import get_redis_connection

from .models import Order, OrderDetail, Course
from .tasks import order_timeout

from logger import log
from coupon.models import CouponLog
from constants import CREDIT_TO_MONEY, ORDER_TIMEOUT


class OrderModelSerializer(serializers.ModelSerializer):
    user_coupon_id = serializers.IntegerField(write_only=True, default=-1)
    order_timeout = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ["pay_type", "id", "order_number", "user_coupon_id", "credit", "order_timeout"]
        read_only_fields = ["id", "order_number", "order_timeout"]
        extra_kwargs = {
            "pay_type": {"write_only": True},
            "credit": {"write_only": True},
        }

    def get_validated_data(self, validated_data):
        user = self.context["request"].user
        user_id = user.id
        # 用户支付方式
        pay_type = validated_data.get("pay_type", 0)
        # 判断用户如果使用了优惠券，则优惠券需要判断验证
        user_coupon_id = validated_data.get("user_coupon_id")

        # 本次下单时，用户使用的优惠券
        user_coupon = None
        if user_coupon_id != -1:
            user_coupon = CouponLog.objects.filter(
                pk=user_coupon_id, user_id=user_id, is_deleted=False, is_show=True
            ).first()

        # 本次下单时使用的积分数量
        use_credit = validated_data.get("credit", 0)
        if use_credit > 0 and use_credit > user.credit:
            raise serializers.ValidationError(detail="您拥有的积分不足以抵扣本次下单的积分，请重新下单！")

        return user, user_id, pay_type, user_coupon_id, user_coupon, use_credit

    def create_order(self, redis, user_id, pay_type):
        # 创建订单记录
        order = Order.objects.create(
            name="购买课程",  # 订单标题
            user_id=user_id,  # 当前下单的用户ID
            order_number=datetime.now().strftime("%Y%m%d") + ("%08d" % user_id) + "%08d" % redis.incr(
                "order_number"),  # 基于redis生成分布式唯一订单号
            pay_type=pay_type,  # 支付方式,默认是支付宝支付
        )

        # 记录本次下单的商品列表
        cart_hash = redis.hgetall(f"cart_{user_id}")
        if len(cart_hash) < 1:
            raise serializers.ValidationError(detail="购物车没有要下单的商品")

        return order, cart_hash

    def discount_credit(self, cart_hash, order, user_coupon, use_credit, user):
        # 提取购物车中所有勾选状态为b'1'的商品
        course_id_list = [int(key.decode()) for key, value in cart_hash.items() if value == b'1']

        # 筛选出要购买的所有课程
        course_list = Course.objects.filter(pk__in=course_id_list, is_deleted=False, is_show=True).all()

        detail_list = []
        total_price = 0  # 本次订单的总价格
        real_price = 0  # 本次订单的实付总价

        # 用户使用优惠券或积分以后，需要在服务端计算本次使用优惠券或积分的最大优惠额度
        total_discount_price = 0  # 总优惠价格
        max_discount_course = None  # 享受最大优惠的课程

        # 本次下单最多可以抵扣的积分
        max_use_credit = 0

        for course in course_list:
            discount_price = course.discount.get("price", None)  # 获取课程原价
            discount_name = course.discount.get("type", "")
            detail_list.append(OrderDetail(
                order=order,
                course=course,
                name=course.name,
                price=course.price,
                real_price=float(course.price if discount_price is None else discount_price),
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

            # 添加每个课程的可用积分
            if use_credit > 0 and course.credit > 0:
                max_use_credit += course.credit

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
            else:
                raise exceptions.ValidationError("优惠方式错误.")

        if use_credit > 0:
            if max_use_credit < use_credit:
                raise exceptions.ValidationError("本次使用的抵扣积分数额超过了限制.")

            # 当前订单添加积分抵扣的数量
            order.credit = use_credit
            total_discount_price = float(use_credit / CREDIT_TO_MONEY)

            # todo 扣除用户拥有的积分，后续在订单超时未支付，则返还订单中对应数量的积分给用户。如果订单成功支付，则添加一个积分流水记录。
            user.credit = user.credit - use_credit
            user.save()

        # 一次性批量添加本次下单的商品记录
        OrderDetail.objects.bulk_create(detail_list)

        # 保存订单的总价格和实付价格
        order.total_price = total_price
        order.real_price = float(real_price - total_discount_price)
        order.save()

    def delete_cart(self, redis, user_id, cart_hash):
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

    def bind_discount_and_order(self, user_coupon, order, user_id, user_coupon_id):
        # 如果有使用了优惠券，则把优惠券和当前订单进行绑定
        if user_coupon:
            user_coupon.order = order
            user_coupon.save()
            # 使用过后，把优惠券从redis中移除
            redis = get_redis_connection("coupon")
            redis.delete(f"{user_id}:{user_coupon_id}")

    def handle_order(self, order):
        # 将来订单状态发生改变，再修改优惠券的使用状态，如果订单过期，则再次还原优惠券到redis中
        order_timeout.apply_async(kwargs={"order_id": order.id}, countdown=ORDER_TIMEOUT)
        # 返回订单超时时间
        order.order_timeout = ORDER_TIMEOUT

    def create(self, validated_data):
        """创建订单"""
        redis = get_redis_connection("cart")
        # 获取数据
        user, user_id, pay_type, user_coupon_id, user_coupon, use_credit = self.get_validated_data(validated_data)
        # 开始事务
        with transaction.atomic():
            # 设置事务回滚的标记点,一个事物中可以设置多个回滚标记
            transaction_start = transaction.savepoint()
            try:
                # 创建订单
                order, cart_hash = self.create_order(redis, user_id, pay_type)
                # 订单折扣和积分优惠
                self.discount_credit(cart_hash, order, user_coupon, use_credit, user)
                # 删除购物车中被勾选的商品，保留没有被勾选的商品信息
                self.delete_cart(redis, user_id, cart_hash)
                # 把优惠券和当前订单进行绑定
                self.bind_discount_and_order(user_coupon, order, user_id, user_coupon_id)
                # 处理订单其余的操作
                self.handle_order(order)
                return order

            except Exception as e:
                log.error(f"订单创建失败：{e}")
                transaction.savepoint_rollback(transaction_start)
                raise exceptions.ValidationError("订单创建失败.")


class OrderDetailMdoelSerializer(serializers.ModelSerializer):
    """订单详情序列化器"""
    # 通过source修改数据源，可以把需要调用的部分外键字段提取到当前序列化器中
    course_id = serializers.IntegerField(source="course.id")
    course_name = serializers.CharField(source="course.name")
    course_cover = serializers.ImageField(source="course.course_cover")

    class Meta:
        model = OrderDetail
        fields = ["id", "price", "real_price", "discount_name", "course_id", "course_name", "course_cover"]


class OrderListModelSerializer(serializers.ModelSerializer):
    """订单列表序列化器"""
    order_courses = OrderDetailMdoelSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "order_number", "total_price", "real_price", "pay_time", "created_time", "credit", "coupon",
                  "pay_type", "order_status", "order_courses"]

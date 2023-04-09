from datetime import datetime

from django.db import transaction

from rest_framework.viewsets import ViewSet

from coupon.models import CouponLog
from orders.models import Order
from user.models import UserCourse, Credit
from course.serializers import CourseInfoModelSerializer

from logger import log
from response import APIResponse
from pay_api import AliPaySDK
from return_code import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR


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

        alipay = AliPaySDK()
        link = alipay.page_pay(order_number, order.real_price, order.name)

        return APIResponse(data={
            "pay_type": 0,  # 支付类型
            "get_pay_type_display": "支付宝",  # 支付类型的提示
            "link": link  # 支付连接地址
        })

    def return_result(self, request):
        """支付宝支付结果的同步通知处理"""
        data = request.query_params.dict()  # QueryDict
        alipay = AliPaySDK()
        success = alipay.check_sign(data)
        if not success:
            return APIResponse(HTTP_400_BAD_REQUEST, "通知结果不存在.")

        order_number = data.get("out_trade_no")
        try:
            order = Order.objects.get(order_number=order_number)
            if order.order_status > 1:
                return APIResponse(HTTP_400_BAD_REQUEST, "订单超时或已取消.")
        except Order.DoesNotExist:
            return APIResponse(HTTP_400_BAD_REQUEST, "订单不存在.")

        # 获取当前订单相关的课程信息，用于返回给客户端
        order_courses = order.order_courses.all()
        course_list = [item.course for item in order_courses]

        if order.order_status == 0:
            result = alipay.query(order_number)
            print(f"result-{result}")

            if result.get("trade_status", None) in ["TRADE_FINISHED", "TRADE_SUCCESS"]:
                """支付成功"""
                with transaction.atomic():
                    save_id = transaction.savepoint()
                    try:
                        now_time = datetime.now()
                        # 1. 修改订单状态
                        order.pay_time = now_time
                        order.order_status = 1
                        order.save()

                        # 2.1 记录扣除个人积分的流水信息
                        if order.credit > 0:
                            Credit.objects.create(operation=1, number=order.credit, user=order.user)
                        # 2.2 补充个人的优惠券使用记录
                        coupon_log = CouponLog.objects.filter(order=order).first()
                        if coupon_log:
                            coupon_log.use_time = now_time
                            coupon_log.use_status = 1  # 1 表示已使用
                            coupon_log.save()

                        # 3. 用户和课程的关系绑定
                        user_course_list = []
                        for course in course_list:
                            user_course_list.append(UserCourse(course=course, user=order.user))
                        UserCourse.objects.bulk_create(user_course_list)

                        # todo 4. 取消订单超时

                    except Exception as e:
                        log.error(f"订单支付处理同步结果发生未知错误：{e}")
                        transaction.savepoint_rollback(save_id)
                        return APIResponse(HTTP_500_INTERNAL_SERVER_ERROR, "当前订单支付未完成，请联系客服工作人员.")

        # 返回客户端结果
        serializer = CourseInfoModelSerializer(course_list, many=True)

        return APIResponse(data={
            "pay_time": order.pay_time.strftime("%Y-%m-%d %H:%M:%S"),
            "real_price": float(order.real_price),
            "course_list": serializer.data
        })

    def query(self, request, order_number):
        """主动查询订单支付的支付结果"""
        try:
            order = Order.objects.get(order_number=order_number)
            if order.order_status > 1:
                return APIResponse(HTTP_400_BAD_REQUEST, "订单超时或已取消.")
        except Order.DoesNotExist:
            return APIResponse(HTTP_400_BAD_REQUEST, "订单不存在.")

        # 获取当前订单相关的课程信息，用于返回给客户端
        order_courses = order.order_courses.all()
        course_list = [item.course for item in order_courses]
        courses_list = []
        for course in course_list:
            courses_list.append(UserCourse(course=course, user=order.user))

        if order.order_status == 0:
            # 请求支付宝，查询订单的支付结果
            alipay = AliPaySDK()
            result = alipay.query(order_number)
            if result.get("trade_status", None) in ["TRADE_FINISHED", "TRADE_SUCCESS"]:
                """支付成功"""
                with transaction.atomic():
                    save_id = transaction.savepoint()
                    try:
                        now_time = datetime.now()
                        # 1. 修改订单状态
                        order.pay_time = now_time
                        order.order_status = 1
                        order.save()
                        # 2.1 记录扣除个人积分的流水信息
                        if order.credit > 0:
                            Credit.objects.create(operation=1, number=order.credit, user=order.user)

                        # 2.2 补充个人的优惠券使用记录
                        coupon_log = CouponLog.objects.filter(order=order).first()
                        if coupon_log:
                            coupon_log.use_time = now_time
                            coupon_log.use_status = 1  # 1 表示已使用
                            coupon_log.save()

                        # 3. 用户和课程的关系绑定
                        user_course_list = []
                        for course in course_list:
                            user_course_list.append(UserCourse(course=course, user=order.user))
                        UserCourse.objects.bulk_create(user_course_list)

                    except Exception as e:
                        log.error(f"订单支付处理同步结果发生未知错误：{e}")
                        transaction.savepoint_rollback(save_id)
                        return APIResponse(HTTP_500_INTERNAL_SERVER_ERROR, "当前订单支付未完成，请联系客服工作人员.")
            else:
                """当前订单未支付"""
                return APIResponse(HTTP_400_BAD_REQUEST, "当前订单未支付.")

        return APIResponse(message="当前订单已支付.")

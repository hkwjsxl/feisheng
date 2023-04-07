from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .services import get_user_coupon_list, get_user_enable_coupon_list

from response import APIResponse


class CouponListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """获取用户拥有的所有优惠券"""
        user_id = request.user.id
        coupon_data = get_user_coupon_list(user_id)
        print(coupon_data)
        return APIResponse(data=coupon_data)


class EnableCouponListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """获取用户拥有的本次下单可用所有优惠券"""
        user_id = request.user.id
        coupon_data = get_user_enable_coupon_list(user_id)
        print(coupon_data)
        return APIResponse(data=coupon_data)

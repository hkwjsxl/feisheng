from django.urls import path

from . import views

urlpatterns = [
    # 获取用户拥有的所有优惠券
    path("", views.CouponListAPIView.as_view()),
    # 获取用户拥有的本次下单可用所有优惠券
    path("enable/", views.EnableCouponListAPIView.as_view()),
]

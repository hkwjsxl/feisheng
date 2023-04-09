from django.urls import path

from . import views

urlpatterns = [
    # 生成支付链接
    path("alipay/<int:order_number>/", views.AlipayAPIViewSet.as_view({"get": "link"})),
    # 支付结果的同步处理
    path("alipay/result/", views.AlipayAPIViewSet.as_view({"get": "return_result"})),
    # 客户端主动查询支付结果是否成功
    path("alipay/query/<int:order_number>/", views.AlipayAPIViewSet.as_view({"get": "query"})),
    # 支付结果的异步处理（只有线上才管用）
    path("alipay/notify/", views.AlipayAPIViewSet.as_view({"post": "notify_result"})),
]

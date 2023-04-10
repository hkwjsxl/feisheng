from django.urls import path

from . import views

urlpatterns = [
    # 创建订单
    path("", views.OrderCreateAPIView.as_view({"post": "create"})),
    # 查看订单状态
    path("pay/status/", views.OrderPayChoicesAPIView.as_view()),
    # 获取订单详情
    path("list/", views.OrderListAPIView.as_view({"get": "list"})),
    # 取消订单
    path("<int:pk>/", views.OrderViewSet.as_view({"put": "pay_cancel"})),
]

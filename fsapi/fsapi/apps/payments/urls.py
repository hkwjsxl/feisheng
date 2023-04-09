from django.urls import path

from . import views

urlpatterns = [
    path("alipay/<int:order_number>/", views.AlipayAPIViewSet.as_view({"get": "link"})),
    path("alipay/result/", views.AlipayAPIViewSet.as_view({"get": "return_result"}))
]

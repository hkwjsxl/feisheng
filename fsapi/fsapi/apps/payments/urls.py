from django.urls import path

from . import views

urlpatterns = [
    path("alipay/<int:order_number>/", views.AlipayAPIViewSet.as_view({"get": "link"})),
]

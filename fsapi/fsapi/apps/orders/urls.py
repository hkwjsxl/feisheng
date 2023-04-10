from django.urls import path

from . import views

urlpatterns = [
    path("", views.OrderCreateAPIView.as_view({"post": "create"})),
    path("pay/status/", views.OrderPayChoicesAPIView.as_view()),
    path("list/", views.OrderListAPIView.as_view({"get": "list"})),
    path("<int:pk>/", views.OrderViewSet.as_view({"put": "pay_cancel"})),
]

from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views

# router = SimpleRouter()
# router.register("", views.OrderCreateAPIView)

urlpatterns = [
    path("", views.OrderCreateAPIView.as_view({"post": "create"}))
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.OrderCreateAPIView.as_view()),
]

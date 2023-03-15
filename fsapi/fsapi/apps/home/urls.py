from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('nav/header', views.NavHeaderListAPIView)
router.register('nav/footer', views.NavFooterListAPIView)

urlpatterns = [

]

urlpatterns += router.urls

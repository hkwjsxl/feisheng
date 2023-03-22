from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('direction', views.CourseDirectionGenericAPIView)

urlpatterns = [

]
urlpatterns += router.urls

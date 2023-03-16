from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
# router.register('', views.)

urlpatterns = [

]

urlpatterns += router.urls

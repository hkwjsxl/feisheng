from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from . import views

router = SimpleRouter()
router.register('register', views.UserRegisterGenericAPIView)

urlpatterns = [
    path("login/", obtain_jwt_token, name="login"),
    path('mobile/<str:mobile>/', views.MobileAPIView.as_view(), name='mobile'),
    path('sms/<str:mobile>/', views.SMSAPIView.as_view(), name='sms'),
    path('login/sms/', views.UserLoginSMSGenericAPIView.as_view(), name='login_sms'),

    # 我的课程列表
    path("course/", views.CourseListAPIView.as_view({"get": "list"})),
]

urlpatterns += router.urls

# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
# obtain_jwt_token实际上就是 rest_framework_jwt.views.ObtainJSONWebToken.as_view()
# 登录视图，获取access_token
# obtain_jwt_token = ObtainJSONWebToken.as_view()
# 刷新token视图，依靠旧的access_token生成新的access_token
# refresh_jwt_token = RefreshJSONWebToken.as_view()
# 验证现有的access_token是否有效
# verify_jwt_token = VerifyJSONWebToken.as_view()

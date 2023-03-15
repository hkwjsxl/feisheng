from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve  # 静态文件代理访问模块

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),

    path('home/', include(('home.urls', 'home'), namespace='home')),
]

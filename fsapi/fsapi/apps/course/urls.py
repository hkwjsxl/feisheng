from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
# 课程方向
router.register('direction', views.CourseDirectionGenericAPIView)
# 课程分类
router.register('category', views.CourseCategoryGenericAPIView)
# 课程列表
router.register('', views.CourseInfoGenericAPIView)
# 课程搜索
router.register("search", views.CourseSearchViewSet, basename="course-search")

urlpatterns = [
    # 搜索热度关键词
    path("search/hot/", views.HotWordAPIView.as_view()),
    # 单个课程详情
    path("<int:pk>/", views.CourseRetrieveAPIView.as_view()),
    # 课程章节的列表
    path("<int:course>/chapter/", views.CourseChapterListAPIView.as_view()),
    # 课程类型
    path("type/", views.CourseTypeListAPIView.as_view()),
]
urlpatterns += router.urls

from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('direction', views.CourseDirectionGenericAPIView)
router.register('category', views.CourseCategoryGenericAPIView)
router.register('', views.CourseInfoGenericAPIView)
router.register("search", views.CourseSearchViewSet, basename="course-search")

urlpatterns = [
    path("search/hot/", views.HotWordAPIView.as_view()),
]
urlpatterns += router.urls

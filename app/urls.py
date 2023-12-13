from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views
from oauth2_provider import views as oauth2_views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('categories', views.CategoryViewSet)
router.register('lessons', views.LessonViewSet)
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("oauth2/token/", oauth2_views.TokenView.as_view(), name="token"),
    #path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
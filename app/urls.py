from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('categories', views.CategoryViewSet)
router.register('lessons', views.LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
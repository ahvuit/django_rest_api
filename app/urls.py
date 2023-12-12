from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
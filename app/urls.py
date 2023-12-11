from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()
router.register('app', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
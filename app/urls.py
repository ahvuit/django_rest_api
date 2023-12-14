from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views
from oauth2_provider import views as oauth2_views

from app.views import CategoryDetailView

router = DefaultRouter()
router.register('register', views.RegisterViewSet)
router.register('categories', views.CategoryViewSet)
router.register('lessons', views.LessonViewSet)
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("oauth2/token/", oauth2_views.TokenView.as_view(), name="token"),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    #path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
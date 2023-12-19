from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app import views
from app.views import CategoryDetailView, LoginViewSet, RegisterViewSet

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('lessons', views.LessonViewSet)
router.register('courses', views.CourseViewSet)

api_url_patterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(api_url_patterns)),
    path('register/', RegisterViewSet.as_view(), name='register'),
    path('login/', LoginViewSet.as_view(), name='login'),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
]
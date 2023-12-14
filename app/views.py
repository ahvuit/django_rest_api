from django.contrib.auth import authenticate, login
from oauth2_provider.oauth2_validators import AccessToken
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from app.serializer import UserSerializer, CategorySerializer, LessonSerializer, CourseSerializer
from app.models import User, Category, Lesson, Course, BaseResponse
from rest_framework import generics
from rest_framework import permissions


class RegisterViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            BaseResponse(message="User created successfully", data=serializer.data, code=201).to_json(),
            status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), permissions.IsAdminUser()]


class CategoryDetailView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

    def create(self, request, *args, **kwargs):
        try:
            # Validate request data
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            # Save data into database
            self.perform_create(serializer)

            # Return a custom response with category data and message
            return Response(
                BaseResponse(message="Category created successfully", data=serializer.data, code=201).to_json(),
                status=status.HTTP_201_CREATED)
        except ValidationError as exc:
            error_message = str(exc.detail.get('name')[0]) if 'name' in exc.detail else 'Validation error'
            return Response(BaseResponse(message=error_message, data=[], code=400).to_json(),
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(BaseResponse(message=str(e), data=[], code=400).to_json(),
                            status=status.HTTP_400_BAD_REQUEST)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

from django.http import JsonResponse
from rest_framework import viewsets
from app.serializer import UserSerializer, CategorySerializer
from app.models import User, Category


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
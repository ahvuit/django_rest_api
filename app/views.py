from django.http import JsonResponse
from rest_framework import viewsets
from app.serializer import UserSerializer
from app.models import User


# Create your views here.

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
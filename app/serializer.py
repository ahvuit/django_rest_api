from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from app.models import User, Category, Lesson, Course


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(ModelSerializer):
    password = CharField(
        max_length=68, min_length=6, write_only=True)
    username = CharField(
        max_length=255, min_length=3)

    tokens = SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['username','password','tokens']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        # return {
        #     'email': user.email,
        #     'username': user.username,
        #     'tokens': user.tokens
        # }

        return super().validate(attrs)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'content', 'active', 'course']


class CourseSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = ['id', 'subject', 'description', 'active', 'category']

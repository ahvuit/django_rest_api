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

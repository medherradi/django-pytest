from rest_framework import serializers
from ..models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'likes', 'count_likes']

    def create(self, validated_data):
        return super().create(validated_data)

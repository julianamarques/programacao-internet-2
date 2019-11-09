from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Adress, Post, User, Comment


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class AdressSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Adress
        fields = '__all__'


class UserPostSerializer(HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class PostsCommentsSerializer(HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

# for explanation of code below see:
# http://www.django-rest-framework.org/tutorial/1-serialization/

from rest_framework import serializers
from articles.models import Image, Comment, Article, Topic, Publication
from django.contrib.auth.models import User

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ('id', 'url', 'article')

class CommentSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Comment
		fields = ('id', 'body', 'date', 'article', 'owner')

class ArticleSerializer(serializers.ModelSerializer):
    images = serializers.SlugRelatedField(many=True, read_only=True, slug_field='url')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #queryset=Comment.objects.all())
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'body', 'date', 'url', 'topic', 'publication', 'images', 'comments')

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', 'description')

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'name', 'logo', 'description')

class UserSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #queryset=Comment.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'comments')
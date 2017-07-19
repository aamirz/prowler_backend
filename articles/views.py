# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q

from articles.models import Image, Comment, Article, Topic, Publication
from django.contrib.auth.models import User
from articles.serializers import ImageSerializer, CommentSerializer, \
								 ArticleSerializer, TopicSerializer, \
								 PublicationSerializer, UserSerializer

from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from articles.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
import django_filters

def docs(request):
    template = loader.get_template('articles/docs.html')
    return HttpResponse(template.render())


########################### USERS ##################################
class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


########################### IMAGES #################################
class ImageList(generics.ListCreateAPIView):
    """
    List all images, or create a new image.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Image.objects.all().order_by('id')
    serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a image instance.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Image.objects.all()
    serializer_class = ImageSerializer 


########################### COMMENTS ###############################

class CommentList(generics.ListCreateAPIView):
    """
    List all comments, or create a new comment.
    """
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Comment.objects.all().order_by('-date')
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a comment instance.
    """
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 

########################### ARTICLES #################################

class ArticleFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    body = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Article
        fields = ['title', 'author', 'body', 'topic', 'publication']


class ArticleList(generics.ListCreateAPIView):
    """
    List all articles, or create a new article.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Article.objects.all().order_by('-date')
    serializer_class = ArticleSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ArticleFilter

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# @api_view(['GET']) 
# def article_search(request, format=None):
#     title = request.GET.get("title", "")
#     author = request.GET.get("author", "")
#     body = request.GET.get("body", "")
#     topic = request.GET.get("topic", None)
#     publication = request.GET.get("publication", None)

#     try:
#         articles = Article.objects.filter(Q(title__icontains=title) | Q(author__icontains=author) | Q(body__icontains=body))
#         if topic is not None:
#             articles.filter(publication=publication) 
#         if publication is not None:
#             articles.filter(topic=topic)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)


@api_view(['GET'])
def article_id(request, pk, format=None):
    """
    Retrieve an article instance.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

@api_view(['GET'])
def article_topic(request, topic_pk, format=None):
    """
    Get articles with the topic given
    """
    if request.method == 'GET':
        articles = Article.objects.filter(topic=topic_pk)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def article_publication(request, publication_pk, format=None):
    """
    Get articles from the publication given
    """
    if request.method == 'GET':
        articles = Article.objects.filter(publication=publication_pk)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def article_year(request, y, format=None):
	"""
	Retrieve articles by year
	"""
	if request.method == 'GET':
		articles = Article.objects.filter(date__year=y)
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def article_month(request, y, m, format=None):
	"""
	Retrieve articles by month
	"""
	if request.method == 'GET':
		articles = Article.objects.filter(date__month=m)
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def article_day(request, y, m, d, format=None):
	"""
	Retrieve articles by year
	"""
	if request.method == 'GET':
		articles = Article.objects.filter(date__day=d)
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def article_title(request, query, format=None):
	"""
	Retrieve articles by title string
	"""
	if request.method == 'GET':
		articles = Article.objects.filter(title__icontains=query)
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def article_body(request, query, format=None):
	"""
	Retrieve articles by body string
	"""
	if request.method == 'GET':
		articles = Article.objects.filter(body__icontains=query)
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def article_author(request, query, format=None):
	"""
	Retrieve articles by author string
	"""
	if request.method == 'GET':
		articles = Article.objects.filter(author__icontains=query)
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

########################### TOPICS ###################################

class TopicList(generics.ListCreateAPIView):
    """
    List all topics, or create a new topic.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Topic.objects.all().order_by('name')
    serializer_class = TopicSerializer

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a topic instance.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

########################### PUBLICATIONS #############################

class PublicationList(generics.ListCreateAPIView):
    """
    List all publications, or create a new publication.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Publication.objects.all().order_by('name')
    serializer_class = PublicationSerializer

class PublicationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a publication instance.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


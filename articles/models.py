# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# class User(models.Model):
#     name  = models.CharField(max_length=100, default='')
#     email = models.CharField(max_length=100, default='')

class Image(models.Model):
    url     = models.CharField(max_length=500, default='')
    article = models.ForeignKey('Article', related_name='images', on_delete=models.CASCADE)

class Comment(models.Model):
    body    = models.CharField(max_length=1000, default='')
    date    = models.DateTimeField('Date published')
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)
    owner   = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)

class Article(models.Model):
    title       = models.CharField(max_length=100, default='')
    author      = models.CharField(max_length=100, default='')
    body        = models.CharField(max_length=60000, default='')
    date        = models.DateTimeField('Date published')
    url         = models.CharField(max_length=500, default='')
    topic       = models.ForeignKey('Topic', on_delete=models.CASCADE)
    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)

class Topic(models.Model):
    name        = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=1000, default='')

class Publication(models.Model):
    name        = models.CharField(max_length=100, default='')
    logo        = models.CharField(max_length=500, default='')
    description = models.CharField(max_length=1000, default='')

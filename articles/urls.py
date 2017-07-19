from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.docs),
    url(r'^docs/$', views.docs),
    ####################### USERS ##########################
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    ####################### IMAGES ##########################
    url(r'^images/$', views.ImageList.as_view()),
    url(r'^images/(?P<pk>[0-9]+)/$', views.ImageDetail.as_view()),
    ####################### COMMENTS ########################
    url(r'^comments/$', views.CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    ####################### ARTICLES ########################
    url(r'^articles/$', views.ArticleList.as_view()),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
    url(r'^articles/topic/(?P<topic_pk>[0-9]+)/$', views.article_topic),
    url(r'^articles/publication/(?P<publication_pk>[0-9]+)/$', views.article_publication),
    url(r'^articles/date/(?P<y>[0-9]{4})/$', views.article_year),
    url(r'^articles/date/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.article_month),
    url(r'^articles/date/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/(?P<d>[0-9]{2})/$', views.article_day),
    url(r'^articles/title/(?P<query>.+)/$', views.article_title),
    url(r'^articles/body/(?P<query>.+)/$', views.article_body),
    url(r'^articles/author/(?P<query>.+)/$', views.article_author),
    ####################### TOPICS ##########################
    url(r'^topics/$', views.TopicList.as_view()),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.TopicDetail.as_view()),
    ####################### PUBLICATIONS ####################
    url(r'^publications/$', views.PublicationList.as_view()),
    url(r'^publications/(?P<pk>[0-9]+)/$', views.PublicationDetail.as_view()),
]

# allow for suffixes that indicate type of data for requests
urlpatterns = format_suffix_patterns(urlpatterns)
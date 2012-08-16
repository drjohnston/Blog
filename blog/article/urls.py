from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.article.models import Article, Person

urlpatterns = patterns('blog.article.views',

    #For now this is the same generic list as at '/', but this will likely 
    #change in the future
    url(r'^$', 
        ListView.as_view(
            queryset=Article.objects.order_by('-datetime')[:10],
            context_object_name = 'latest_articles_list',
            template_name = 'article/index.html'),
        name='article_index'),

    #Generic view for author profile
    url(r'^author/(?P<pk>\d+)/$', 
        DetailView.as_view(
            model=Person,
            template_name='article/author.html'),
        name="author"),

    #Custom views
    url(r'^(?P<article_id>\d+)/$', 'detail'),
    url(r'^(?P<article_id>\d+)/comment/$', 'make_comment'),
    #url(r'^(?P<article_id>\d+)/vote/$', 'vote'),
    )

from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from blog.article.models import Article
from blog.article import urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #generic list view for '/'
    url(r'^$', 
        ListView.as_view(
            queryset=Article.objects.order_by('-datetime')[:10],
            context_object_name='latest_articles_list',
            template_name='article/index.html'),
        name='article_index'),

    url(r'^article/', include('blog.article.urls')),

    #auth; login and logout use generic views, register uses custom view
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page': '/'}, name='logout'),
    url(r'^register/$', 'blog.views.register', name='register'),

    #admin
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib import admin
from blog.article.models import *

admin.site.register(Article)
admin.site.register(Person)
admin.site.register(Comment)
admin.site.register(Vote)

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import datetime

class Person(models.Model):
    '''Current functionality could probably be handled by User, but we will need a separate model in the future.'''
    user = models.ForeignKey( User, unique=True )

    def __unicode__(self):
        return unicode(self.user)
        
class Article(models.Model):
    title = models.CharField( max_length=100 )
    content = models.TextField()
    datetime = models.DateTimeField( default=datetime.now )
    author = models.ForeignKey( Person, related_name="article_author" )

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField( max_length=100, blank=True, null=True )
    content = models.TextField()
    datetime = models.DateTimeField( default=datetime.now )
    commenter = models.ForeignKey( Person, related_name="comment_author" )
    article = models.ForeignKey( Article )

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.pk

class PartialCommentForm(ModelForm):
    '''We only need commenters to provide the title and the content. All other fields are auto-populated.'''
    class Meta:
        model = Comment
        fields = ('title', 'content')

class Vote(models.Model):
    '''This model is to keep a record of who is voting for what so we can prevent double votes etc.'''
    value = models.IntegerField()
    datetime = models.DateTimeField ( default=datetime.now )
    voter = models.ForeignKey( Person, related_name="vote_author" )
    article = models.ForeignKey( Article ) 

    def __unicode__(self):
        return str(self.value)
    

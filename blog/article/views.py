from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from blog.article.models import *

def detail(request, article_id):
    """Article detail view that passes a blank instance of the
    PartialCommentForm to the template. Could potentially make this
    view generic."""
    article = get_object_or_404(Article, pk=article_id)
    form = PartialCommentForm() #blank form
    return render_to_response('article/detail.html', locals(),
                              context_instance=RequestContext(request))

@login_required
def make_comment(request, article_id):
    '''Only authenticated users can comment. The user supplies the
    'title' and 'content' through the PartialCommentForm; we supply
    the 'commenter' and 'article' field. The 'datetime' field is
    handled by default with the 'default=datetime.now' setting in
    models.py.'''
    article = get_object_or_404(Article, pk=article_id)
    commenter = request.user.get_profile()

    if request.method == 'POST':
        form = PartialCommentForm(request.POST)

        #Create form without saving it
        f = form.save(commit=False)

        #Populate form with the data we already have (datetime is done by default)
        f.article = article
        f.commenter = commenter
        f.save()

        #Process form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog.article.views.detail', args=(article.id,)))
        else:
            #send user back to detail
            return redirect(detail, article.id)
                        
    else:
        #redirect to detail
        return redirect(detail, article.id)
        

###To do:
#@login_required
#def vote(request, article_id):

    

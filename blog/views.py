from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext

def register(request):
    '''This is a simple registration view that makes use of django's
    built-in UserCreationForm.  After saving the form, we create a
    person record for the new user.'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            #attach user record to a person record
            new_user.person_set.create(pk=new_user.pk)

            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", locals(),
                              context_instance=RequestContext(request))

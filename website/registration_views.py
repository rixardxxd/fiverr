__author__ = 'xxd'

from forms import LoginForm, SignupForm
from django.contrib.auth import logout, login
from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.template import RequestContext

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def login_view(request):
    #default to main page
    next = '/'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user and user.is_active:
                #do the real login
                login(request, user)
            #redirect
            return HttpResponseRedirect(request.POST.get('next'))
        else:
            print 'invalid login'
    else:
        form = LoginForm()
        if request.method == 'GET' and 'next' in request.GET:
            next = request.GET.get('next')
    context_dict = {
        'form': form,
        'next': next
    }
    return render_to_response("registration/login.html", RequestContext(request, context_dict))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def register_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #we need to
            if new_user and new_user.is_active:
                #do the real login
                login(request, new_user)
            #redirect to the next page
            return HttpResponseRedirect('/')
        else:
            print 'invalid'
    else:
        form = SignupForm()
    context_dict = {
        'form': form,
        'next': next
    }
    return render_to_response("registration/register.html", RequestContext(request, context_dict))

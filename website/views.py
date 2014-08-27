from django.shortcuts import render
from django.shortcuts import render_to_response, render, HttpResponseRedirect, redirect
from django.template import RequestContext

def main_view(request):
    context_dict = {}
    return render_to_response('website/main.html',RequestContext(request, context_dict))
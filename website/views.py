# -*- coding: utf-8 -*-
# coding=gbk
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from website.models import Gig


def main_view(request):
    gigs = Gig.objects.select_related('Image').all()
    gigs = Gig.objects.select_related('Image').all()

    print gigs
    gig_list_2d = list()
    print len(gigs)
    print range(len(gigs))
    for i in range(len(gigs)):
        gig_list_2d.append(list())
    print gig_list_2d
    for i, gig in enumerate(gigs):
        gig_list_2d[i/3].append(gig)
    print "/////////////////////////////////"
    print gig_list_2d
    print "/////////////////////////////////"
    context_dict = {'gig_list_2d': gig_list_2d}
    return render_to_response('website/main_view.html', RequestContext(request, context_dict))


def gig_view(request, gigid):
    gig = Gig.objects.select_related('category').select_related('sub_category').get(id=gigid)
    if gig is not None:
        context_dict = {'gig': gig}
        return render_to_response('website/gig_view.html', RequestContext(request, context_dict))
    else:
        raise Http404


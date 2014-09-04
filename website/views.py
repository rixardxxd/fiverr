# -*- coding: utf-8 -*-
# coding=gbk
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from website.models import Gig, Image


def main_view(request):
    gigs = Gig.objects.all()
    for gig in gigs:
        img_list = list(gig.image_set.all())
        if len(img_list) > 0:
            gig.first_img = img_list[0]

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
    try:
        #first join sub_category and then join category
        gig = Gig.objects.select_related('sub_category__category').get(id=gigid)
    except:
        raise Http404
    if gig is not None:
        context_dict = {'gig': gig}
        return render_to_response('website/gig_view.html', RequestContext(request, context_dict))
    else:
        raise Http404


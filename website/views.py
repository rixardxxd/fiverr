# -*- coding: utf-8 -*-
# coding=gbk
from django.shortcuts import render_to_response, render, HttpResponseRedirect, redirect
from django.template import RequestContext

def main_view(request):
    #mock the data right now
    gigs = list()
    gig1 = dict()
    gig1['img'] = '/static/img/img1.jpeg'
    gig1['title'] = u'第一项服务'

    gig2 = dict()
    gig2['img'] = '/static/img/img2.jpeg'
    gig2['title'] = u'第二项服务'

    gig3 = dict()
    gig3['img'] = '/static/img/img3.jpeg'
    gig3['title'] = u'第三项服务'

    gig4 = dict()
    gig4['img'] = '/static/img/img4.jpeg'
    gig4['title'] = u'第四项服务'

    gig5 = dict()
    gig5['img'] = '/static/img/img5.jpeg'
    gig5['title'] = u'第五项服务'

    gigs.append(gig1)
    gigs.append(gig2)
    gigs.append(gig3)
    gigs.append(gig4)
    gigs.append(gig5)
    context_dict = {'gigs':gigs}
    return render_to_response('website/main.html',RequestContext(request, context_dict))
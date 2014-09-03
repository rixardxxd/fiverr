# -*- coding: utf-8 -*-
# coding=gbk
from django.shortcuts import render_to_response, render, HttpResponseRedirect, redirect
from django.template import RequestContext

def main_view(request):
    #mock the data right now
    item_list = list()
    item1 = dict()
    item1['img'] = '/static/img/img1.jpeg'
    item1['name'] = u'第一项服务'

    item2 = dict()
    item2['img'] = '/static/img/img2.jpeg'
    item2['name'] = u'第二项服务'

    item3 = dict()
    item3['img'] = '/static/img/img3.jpeg'
    item3['name'] = u'第三项服务'

    item4 = dict()
    item4['img'] = '/static/img/img4.jpeg'
    item4['name'] = u'第四项服务'

    item5 = dict()
    item5['img'] = '/static/img/img5.jpeg'
    item5['name'] = u'第五项服务'

    item_list.append(item1)
    item_list.append(item2)
    item_list.append(item3)
    item_list.append(item4)
    item_list.append(item5)
    context_dict = {'list_items':item_list}
    return render_to_response('website/main_view.html',RequestContext(request, context_dict))
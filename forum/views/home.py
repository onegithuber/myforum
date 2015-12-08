#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response('page/index.html', {'home': 'This is my house'}, context_instance=RequestContext(request))

#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.http import Http404

from formu import settings


def send_mail(title, content, to):
    msg = EmailMultiAlternatives(title, content, settings.DEFAULT_FROM_EMAIL, [to])
    msg.attach_alternative(content, 'text.html')
    msg.send()


def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404

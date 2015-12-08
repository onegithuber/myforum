#!/usr/bin/python
# -*- coding:utf-8 -*-

from django.conf.urls import url, patterns

from forum.views import common,user

urlpatterns = patterns('',
                       url(r'^register/$', 'forum.views.user.register', name='register'),
                       url(r'^login/$', common.method_splitter, {'GET': user.get_login, 'POST': user.post_login}),
                       url(r'^home/$', 'forum.views.home.home'),
                       )

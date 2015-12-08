#!/usr/bin/python
# -*- coding:utf-8 -*-

from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.template import Context, loader, RequestContext

from formu import settings
from forum.forms.user import RegisterForm, LoginForm
from forum.views.common import send_mail


def get_register(request, **kwargs):
    auth.logout(request)
    return render_to_response('user/register.html', kwargs, context_instance=RequestContext(request))


def register(request):
    form = RegisterForm(request.POST)

    if not form.is_valid():
        return get_register(request, errors=form.errors)

    user = form.save()
    if user:
        mail_title = u'片刻社区注册成功通知'
        mail_content = loader.get_template('user/register_mail.html').render(Context({}))
        send_mail(mail_title, mail_content, user.email)
    return redirect(settings.LOGIN_URL)


# class Register(FormView):
#     template_name = "user/register.html"
#     success_url = "/index"
#     form_class = RegisterForm
#
#     def form_invalid(self, form):
#         form.save()
#         username = form.clean_data.get('username')
#         password = form.clean_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(self.request, user)
#         return super(Register, self).form_invalid(form)


def get_login(request, **kwargs):
    auth.logout(request)
    return render_to_response('user/login.html', kwargs,
                              context_instance=RequestContext(request))


def post_login(request):
    form = LoginForm(request.POST)
    if not form.is_valid():
        return get_login(request, errors=form.errors)

    user = form.get_user()
    auth.login(request, user)

    if user.is_staff:
        return redirect(request.REQUEST.get('next', '/manage/admin/'))

    return redirect(request.REQUEST.get('next', '/'))

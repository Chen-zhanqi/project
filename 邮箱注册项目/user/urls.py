# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/18 11:50'
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register/$', user_register, name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^forget/$', user_forget, name='forget'),
    url(r'^active/(?P<code>\w{16})/$', user_active, name='active'),
    url(r'^modify/(?P<code>\w{16})/$', user_modify, name='modify'),
    url(r'^center/$', user_center, name='center')
]
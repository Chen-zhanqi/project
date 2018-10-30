# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/26 10:57'
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout')
]
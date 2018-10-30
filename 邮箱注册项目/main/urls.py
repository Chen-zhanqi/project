# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/22 14:13'
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index')
]
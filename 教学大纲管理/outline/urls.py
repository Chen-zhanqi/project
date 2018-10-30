# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/25 10:38'
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^list/', outline_list, name='outline_list'),
    url(r'^add/', outline_add, name='outline_add'),
    url(r'^detail/', outline_detail, name='outline_detail'),
    url(r'^edit/', outline_edit, name='outline_update'),
    url(r'^delete/', outline_delete, name='outline_delete'),
]

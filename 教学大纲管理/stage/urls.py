# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/25 10:38'
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^list/', stage_list, name='stage_list'),
    url(r'^add/', stage_add, name='stage_add'),
    url(r'^detail/', stage_detail, name='stage_detail'),
    url(r'^edit/', stage_edit, name='stage_edit'),
    url(r'^delete/', stage_delete, name='stage_delete'),
]

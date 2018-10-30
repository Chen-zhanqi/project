# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/25 10:38'
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^list/', program_list, name='program_list'),
    url(r'^add/', program_add, name='program_add'),
    url(r'^detail/', program_detail, name='program_detail'),
    url(r'^edit/', program_edit, name='program_update'),
    url(r'^delete/', program_delete, name='program_delete'),
]

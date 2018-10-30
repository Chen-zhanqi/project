# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/25 10:38'
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', subject_list, name='subject_list'),
    url(r'^add/', subject_add, name='subject_add'),
    url(r'^detail/$', subject_detail, name='subject_detail'),
    url(r'^edit/$', subject_edit, name='subject_edit'),
    url(r'^delete/$', subject_delete, name='subject_delete'),
]

# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/26 9:38'
from django import forms


class ProgramFrom(forms.Form):
    sign = forms.CharField(max_length=50)
    digest = forms.CharField(max_length=255)
    prepare = forms.CharField(max_length=255)
    process = forms.CharField(max_length=2000)
    attention = forms.CharField(max_length=255)
    exercise = forms.CharField(max_length=255)
    share = forms.CharField(max_length=255)
    management = forms.CharField(max_length=255)
    remark = forms.CharField(max_length=255)






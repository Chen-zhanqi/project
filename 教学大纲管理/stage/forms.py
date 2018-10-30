# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/25 16:22'
from django import forms


class StageForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    days = forms.IntegerField(required=True)
    number = forms.IntegerField(required=True)
    project = forms.CharField(max_length=255, required=True)
    teaching = forms.CharField(max_length=255, required=True)
    learning = forms.CharField(max_length=255, required=True)
    sharing = forms.CharField(max_length=255, required=True)
    remark = forms.CharField(max_length=255, required=True)


# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/25 14:38'
from django import forms


class SubjectForm(forms.Form):

    name = forms.CharField(max_length=30, required=True)
    amount = forms.IntegerField(required=True)
    days = forms.IntegerField(required=True)
    number = forms.IntegerField(required=True)
    assurance = forms.CharField(max_length=50, required=True)
    remark = forms.CharField(max_length=255, required=True)







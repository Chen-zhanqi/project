# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/18 16:07'
# forms 表单验证模块，可以在模板文件中通过python代码实现标签
from django import forms
# 引入验证码模块
from captcha.fields import CaptchaField


class RegisterForm(forms.Form):

    # 验证的form表单字段
    # EmailField() 必须填写email邮箱格式的数据
    # required 表单数据是否为必填项
    # max_length 设置表单最长可以填写多少个字符
    # min_length 设置表单最少填写多少个字符
    email = forms.EmailField(required=True, max_length=20, min_length=10, error_messages={'required':'该项为不能为空！', 'invalid': '输入的邮箱不合法！'})
    #
    pwd1 = forms.CharField(required=True, max_length=20, min_length=6, error_messages={'required':'该项为不能为空！', 'invalid': '密码不合法！'})

    pwd2 = forms.CharField(required=True, max_length=20, min_length=6, error_messages={'required':'该项为不能为空！', 'invalid': '密码不合法！'})

    # 验证码字段
    captcha = CaptchaField(required=True, error_messages={'required': '验证码不能为空', 'invalid': '验证码错误'})


class ForgetForm(forms.Form):

    email = forms.EmailField(max_length=50, required=True)
    captcha = CaptchaField(required=True)


class ModifyForm(forms.Form):

    pwd1 = forms.CharField(max_length=20, min_length=6, required=True)
    pwd2 = forms.CharField(max_length=20, min_length=6, required=True)
    email = forms.EmailField(max_length=50, required=True)
    code = forms.CharField(max_length=16, min_length=16, required=True)


class LoginForm(forms.Form):

    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=20, min_length=6, required=True)
    captcha = CaptchaField(required=True)

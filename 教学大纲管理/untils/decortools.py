# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/29 17:02'
from functools import wraps
from subject.models import SubjectModel
from django.shortcuts import redirect, reverse, HttpResponse


def subject_permission(func):

    @wraps(func)
    def _func(*args, **kwargs):
        request = args[0]

        s_id = request.GET.get('s_id')

        subjects = SubjectModel.objects.filter(id=s_id)

        if subjects:
            # 有权限访问
            if subjects[0] in request.user.subject.all():
                return func(*args, **kwargs)
            else:
                # 没有权限
                return redirect(reverse('subject_list') + '?err=1')
        else:

            return HttpResponse(status=404)

    return _func


def role_permission(roles):

    def permission(func):

        def _func(*args, **kwargs):

            request = args[0]
            if request.user.role in roles:

                return func(*args, **kwargs)
            else:

                return redirect(reverse('subject_list') + '?err=1')

        return _func

    return permission

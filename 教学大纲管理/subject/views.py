from datetime import datetime

from django.contrib.auth.views import login_required
from django.shortcuts import render, redirect, reverse, Http404, HttpResponse
from .models import SubjectModel
from .forms import SubjectForm
from user.models import MyUserModel
from untils.decortools import subject_permission, role_permission
# Create your views here.

@login_required
def subject_list(request):

    context = {
        'title': '学科列表',
    }
    if request.GET.get('err') == '1':
        context['errmsg'] = '无权限访问！'

    subjects = SubjectModel.objects.all().order_by('number')

    context['subjects'] = subjects

    return render(request, 'subject/list.html', context)


@login_required
@subject_permission
def subject_detail(request):
    """
    GET请求需要参数： s_id  学科id 必须
    :param request:
    :return:
    """
    if request.method == 'GET':

        s_id = request.GET.get('s_id')

        if s_id:

            try:
                subject = SubjectModel.objects.get(id=s_id)
                creater = MyUserModel.objects.get(id=subject.creater)
                updater = MyUserModel.objects.get(id=subject.updater)
                context = {
                    'title': f'学科详情-{subject.name}',
                    'subject': subject,
                    'creater': creater,
                    'updater': updater,
                }

                return render(request, 'subject/detail.html', context)
            except Exception as e:

                return Http404
        else:
            # 返回404
            return Http404()




    return render(request, 'subject/detail.html')


@login_required
@subject_permission
@role_permission(roles=(1, 2))
# 访问者必须是学科负责人或者管理员
def subject_edit(request):
    """
    GET 需要 s_id  必须
    :param request:
    :return:
    """
    if request.method == 'GET':

        s_id = request.GET.get('s_id')
        if s_id:
            try:
                subject = SubjectModel.objects.get(id=s_id)
                context = {
                    'title': f'修改学科-{subject.name}',
                    'subject': subject
                }

                return render(request, 'subject/edit.html', context)
            except Exception as e:

                return Http404()

        else:
            return Http404()

    elif request.method == 'POST':

        forms = SubjectForm(request.POST)
        s_id = request.POST.get('s_id')

        if forms.is_valid():
            name = forms.cleaned_data['name']
            subjects = SubjectModel.objects.filter(name=name)
            # 判断查找到的结果和要修改的数据是否一致
            # 判断修改后的名称是否存在
            if subjects and subjects[0].id != int(s_id):

                context = {
                    'title': '添加学科',
                    'forms': forms,
                    'errmsg': '该学科已存在！',
                    'subject': {'id': s_id}
                }

                return render(request, 'subject/edit.html', context)
            else:
                s_id = request.POST.get('s_id')
                # 判断s_id是否存在
                if not s_id or not SubjectModel.objects.filter(id=s_id):

                    return Http404()
                else:

                    subject = SubjectModel.objects.get(id=s_id)
                    subject.name = forms.cleaned_data['name']
                    subject.amount = forms.cleaned_data['amount']
                    subject.days = forms.cleaned_data['days']
                    subject.number = forms.cleaned_data['number']
                    subject.assurance = forms.cleaned_data['assurance']
                    subject.remark = forms.cleaned_data['remark']
                    subject.update_time = datetime.now()
                    # 修改subject.updater 修改人
                    subject.updater = request.user.id
                    subject.save()

                    return redirect(reverse('subject_list'))

        else:

            context = {
                'title': '修改学科-{}'.format(forms.cleaned_data['name']),
                'forms': forms,
                'subject': {'id': s_id}

            }

            return render(request, 'subject/edit.html', context)


@login_required
@role_permission(roles=(2, ))
def subject_delete(request):

    if request.method == 'GET':
        s_id = request.GET.get('s_id')
        if s_id and SubjectModel.objects.filter(id=s_id):
            SubjectModel.objects.get(id=s_id).delete()

            return redirect(reverse('subject_list'))
        else:

            return HttpResponse(status=401)

        return render(request, 'subject/delete.html')


@login_required
def subject_add(request):

    if request.method == 'GET':

        return render(request, 'subject/add.html', {'title': '添加学科'})

    elif request.method == 'POST':

        forms = SubjectForm(request.POST)
        if forms.is_valid():

            # 拿到学科信息
            name = forms.cleaned_data['name']
            # 判断该学科是否存在
            if SubjectModel.objects.filter(name=name):
                context = {
                    'title': '添加学科',
                    'forms': forms,
                    'errmsg': '该学科已存在！'
                }

                return render(request, 'subject/add.html', context)
            else:

                subject = SubjectModel()
                subject.name = forms.cleaned_data['name']
                subject.amount = forms.cleaned_data['amount']
                subject.days = forms.cleaned_data['days']
                subject.number = forms.cleaned_data['number']
                subject.assurance = forms.cleaned_data['assurance']
                subject.remark = forms.cleaned_data['remark']
                subject.creater = request.user.id
                subject.updater = request.user.id
                subject.save()

                # 给管理员该学科权限
                request.user.subject.add(subject)
                request.user.save()
                # 返回列表页面
                # reverse 通过url的name属性值查找路由地址
                return redirect(reverse('subject_list'))

        else:

            context = {
                'title': '添加学科',
                'forms': forms
            }

            return render(request, 'subject/add.html', context)

        return render(request, 'subject/add.html', {'title': '添加学科'})



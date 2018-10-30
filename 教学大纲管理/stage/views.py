from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.views import login_required

from .forms import StageForm
from .models import *
from untils.decortools import subject_permission
# Create your views here.

@login_required
@subject_permission
def stage_list(request):
    """
    参数   s_id 必须  subjectid
    :param request:
    :return:
    """
    if request.method == 'GET':
        s_id = request.GET.get('s_id')

        subject = SubjectModel.objects.get(id=s_id)
        stages = StageModel.objects.filter(subject=subject).order_by('number')

        context = {
            'title': f'学科阶段-{subject.name}',
            'subject': subject,
            'stages': stages
        }
        return render(request, 'stage/list.html', context)


@login_required
def stage_detail(request):

    return render(request, 'stage/detail.html')


@login_required
def stage_edit(request):

    return render(request, 'stage/edit.html')


@login_required
def stage_delete(request):

    return render(request, 'stage/delete.html')


@login_required
def stage_add(request):

    if request.method == 'GET':

        s_id = request.GET.get('s_id')

        if s_id and SubjectModel.objects.filter(id=s_id):
            subject = SubjectModel.objects.get(id=s_id)
            context = {
                'title': f'添加阶段-{subject.name}',
                'subject': subject
            }

            return render(request, 'stage/add.html', context)

        else:

            return HttpResponse(status=401)

    elif request.method == 'POST':

        forms = StageForm(request.POST)
        s_id = request.POST.get('s_id')
        if forms.is_valid():
            # 判断阶段名称是否重复
            stage = StageModel()
            stage.subject_id = s_id
            stage.title = forms.cleaned_data['title']
            stage.days = forms.cleaned_data['days']
            stage.number = forms.cleaned_data['number']
            stage.teaching = forms.cleaned_data['teaching']
            stage.learning = forms.cleaned_data['learning']
            stage.sharing = forms.cleaned_data['sharing']
            stage.remark = forms.cleaned_data['remark']
            stage.project = forms.cleaned_data['project']

            stage.save()
            # 拼接完整的重定向地址，带参数
            return redirect(reverse('stage_list')+f'?s_id={s_id}')

        else:
            subject = SubjectModel.objects.get(id=s_id)
            context = {
                'title': '添加阶段',
                'forms': forms,
                'subject': subject
            }
            return render(request, 'stage/add.html', context)











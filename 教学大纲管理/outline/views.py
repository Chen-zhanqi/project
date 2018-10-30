from django.shortcuts import render,HttpResponse
from django.contrib.auth.views import login_required
from .models import *
# Create your views here.


@login_required
def outline_list(request):
    """
    stage_id  必要   阶段id
    :param request:
    :return:
    """

    stage_id = request.GET.get('stage_id')

    if stage_id and StageModel.objects.filter(id=stage_id):

        # 通过阶段id查找该阶段的一级大纲数据
        stage = StageModel.objects.get(id=stage_id)
        context = {
            'title': f'{stage.title}-一级大纲',
            'outlines': stage.outlinemodel_set.all(),
            'stage': stage
        }

        return render(request, 'outline/list.html', context)
    else:

        return HttpResponse('参数有误！', status=401)


@login_required
def outline_detail(request):

    return render(request, 'outline/detail.html')


@login_required
def outline_edit(request):

    return render(request, 'outline/edit.html')


@login_required
def outline_delete(request):

    return render(request, 'outline/delete.html')


@login_required
def outline_add(request):

    return render(request, 'outline/add.html')


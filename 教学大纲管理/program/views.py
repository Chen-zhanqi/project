from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import login_required
from outline.models import OutlineModel
from .models import ProgramModel
from .forms import ProgramFrom
# Create your views here.


@login_required
def program_list(request):

    o_id = request.GET.get('o_id')

    outline = OutlineModel.objects.get(id=o_id)

    context = {
        'title': '二级大纲-{}'.format(outline.stage.title),
        'outline': outline
    }

    return render(request, 'program/list.html', context)


@login_required
def program_detail(request):

    return render(request, 'program/detail.html')


@login_required
def program_edit(request):

    return render(request, 'program/edit.html')


@login_required
def program_delete(request):

    return render(request, 'program/delete.html')


@login_required
def program_add(request):
    """
    请求方式：
    GET POST PUT DELETE UPDATE HEAD OPTION....
    :param request:
    :return:
    """
    if request.method == 'GET':
        o_id = request.GET.get('o_id')

        outline = OutlineModel.objects.get(id=o_id)
        outline.stage.subject.stagemodel_set

        context = {
            'title': f'添加二级大纲-{outline.stage.subject.name}-{outline.stage.title}-{outline.title}',
            'outline': outline
        }

        return render(request, 'program/add.html', context)
    elif request.method == 'POST':

        stage_id = request.POST.get('stage_id')
        outline_id = request.POST.get('outline_id')

        outline = OutlineModel.objects.get(id=outline_id)

        if outline.stage.id == int(stage_id):

            forms = ProgramFrom(request.POST)

            if forms.is_valid():

                program = ProgramModel()

                program.stage_id = stage_id
                program.outline = outline
                program.sign = forms.cleaned_data['sign']
                program.digest = forms.cleaned_data['digest']
                program.prepare = forms.cleaned_data['prepare']
                program.process = forms.cleaned_data['process']
                program.attention = forms.cleaned_data['attention']
                program.exercise = forms.cleaned_data['exercise']
                program.share = forms.cleaned_data['share']
                program.management = forms.cleaned_data['management']
                program.remark = forms.cleaned_data['remark']
                program.save()

                return redirect(reverse('program_list')+f'?o_id={outline_id}')

            else:
                context = {
                    'title': f'添加二级大纲-{outline.stage.subject.name}-{outline.stage.title}-{outline.title}',
                    'outline': outline
                }
                return render(request, 'program/add.html', context)
        else:
            context = {
                'title': f'添加二级大纲-{outline.stage.subject.name}-{outline.stage.title}-{outline.title}',
                'outline': outline,
                'errmsg': '上传数据有误，请检查！'
            }
            return render(request, 'program/add.html', context)









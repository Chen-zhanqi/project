from django.db import models
from subject.models import *
from outline.models import OutlineModel
from stage.models import StageModel
# Create your models here.


class ProgramModel(PublicModel):
    # 阶段
    stage = models.ForeignKey(StageModel, on_delete=models.CASCADE)
    # 一级大纲
    outline = models.ForeignKey(OutlineModel, on_delete=models.CASCADE)
    sign = models.CharField(max_length=50, verbose_name='标志性内容', default='<无>')
    digest = models.CharField(max_length=255, verbose_name='内容摘要', default='<无>')
    prepare = models.CharField(max_length=255, verbose_name='准备工作', default='<无>')
    process = models.TextField(max_length=2000, verbose_name='讲课流程', default='<无>')
    attention = models.CharField(max_length=255, verbose_name='注意事项', default='<无>')
    exercise = models.CharField(max_length=255, verbose_name='注意事项', default='<无>')
    share = models.CharField(max_length=255, verbose_name='注意事项', default='<无>')
    management = models.CharField(max_length=255, verbose_name='注意事项', default='<无>')
    remark = models.CharField(max_length=255, verbose_name='注意事项', default='<无>')

    class Meta:
        db_table = 'program'


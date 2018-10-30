from django.db import models
from subject.models import PublicModel
from stage.models import StageModel
# Create your models here.


class OutlineModel(PublicModel):

    title = models.CharField(max_length=50, verbose_name='标题')
    days = models.IntegerField(verbose_name='学时')
    advancing = models.CharField(max_length=255, verbose_name='高级内容')
    remark = models.CharField(max_length=255, verbose_name='备注')

    stage = models.ForeignKey(StageModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'outline'



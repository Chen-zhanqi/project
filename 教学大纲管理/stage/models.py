from django.db import models
from subject.models import PublicModel,SubjectModel
# Create your models here.


class StageModel(PublicModel):

    # 学科和阶段一对多关系
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)

    title = models.CharField(max_length=50, default='<无>', verbose_name='阶段标题')
    days = models.IntegerField(verbose_name='学时')
    project = models.CharField(max_length=255, default='<无>', verbose_name='阶段项目')
    teaching = models.CharField(max_length=255, default='<无>', verbose_name='教学方法')
    learning = models.CharField(max_length=255, default='<无>', verbose_name='学习方法')
    sharing = models.CharField(max_length=255, default='<无>', verbose_name='学生分享')
    remark = models.CharField(max_length=255, default='<无>', verbose_name='备注')

    class Meta:
        db_table = 'stage'







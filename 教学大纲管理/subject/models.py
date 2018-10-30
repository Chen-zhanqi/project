from django.db import models


class PublicModel(models.Model):

    status = models.IntegerField(default=0, verbose_name='状态')
    number = models.IntegerField(default=1, verbose_name='顺序')
    creater = models.IntegerField(null=False, default=0, verbose_name='创建者id')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updater = models.IntegerField(null=False, default=0, verbose_name='修改者id')
    update_time = models.DateTimeField(auto_now_add=True)


# Create your models here.
class SubjectModel(PublicModel):

    name = models.CharField(max_length=30, null=False, default='', verbose_name='名称')
    amount = models.IntegerField(null=False, default=0, verbose_name='学费')
    days = models.IntegerField(null=False, default=0, verbose_name='学时')
    assurance = models.CharField(max_length=50, null=False, default='<无>', verbose_name='承诺')
    remark = models.CharField(max_length=255, null=False, default='<无>', verbose_name='备注')

    class Meta:

        db_table = 'subject'

    def __str__(self):

        return self.name






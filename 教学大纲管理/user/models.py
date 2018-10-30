from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from subject.models import SubjectModel


class MyUserModel(AbstractUser):
    """
    role 角色  表示当前这个用户是哪个学科的老师
    1 表示Java
    2 表示Python
    3 表示前端
    4 UI
    5 ....
    role = 0 超级管理员
    """
    subject = models.ManyToManyField(SubjectModel, verbose_name='学科')
    role = models.IntegerField(default=0, choices=((0, '普通用户'), (1, '学科负责人'), (2, '管理员')))
    account = models.CharField(max_length=50, verbose_name='账户信息', default='')
    mobile = models.CharField(max_length=20, verbose_name='手机号', default='')

    class Meta:

        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

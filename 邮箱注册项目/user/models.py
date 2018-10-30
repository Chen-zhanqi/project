from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


# 扩展用户表字段
# 新建类，让该类继承自原始的用户模型
class UserProfile(AbstractUser):
    # 扩展一些额外的字段
    nick_name = models.CharField(max_length=30, verbose_name='用户昵称', null=True, blank=True)
    phone = models.BigIntegerField(verbose_name='用户手机', null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name='用户地址', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='个人简介', null=True, blank=True)

    # class Meta:
    #     db_table = ''


class EmailRecard(models.Model):

    code = models.CharField(max_length=50, null=False, verbose_name='验证码')
    email = models.EmailField(max_length=100, null=False, verbose_name='收件人邮箱')
    # 邮件发送的时间
    # auto_now_add 当创建对象时，自动获取当前之间进行赋值
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='发送时间')
    # 邮件类型 register 注册    forget 找回密码
    # choices 选项， 规定好选项，该属性值只能是选项中的某一个
    # default 默认值
    email_type = models.CharField(max_length=10, choices=(('register', '注册账号'), ('forget', '找回密码')), default='register', verbose_name='邮件类型')
    # 过期时间
    expire_time = models.DateTimeField(verbose_name='过期时间')
    # 邮件状态，邮件是否已使用
    email_status = models.IntegerField(choices=((1, '已使用'), (0, '未使用')), default=0, verbose_name='邮件状态')

    class Meta:
        db_table = 'email_recard'
        # 在后台管理界面中显示名称
        verbose_name = '邮件'
        verbose_name_plural = verbose_name










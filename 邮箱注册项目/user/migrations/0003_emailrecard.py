# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20181018_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailRecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='验证码')),
                ('email', models.EmailField(max_length=100, verbose_name='收件人邮箱')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('email_type', models.CharField(choices=[('register', '注册账号'), ('forget', '找回密码')], default='register', max_length=10, verbose_name='邮件类型')),
                ('expire_time', models.DateTimeField(verbose_name='过期时间')),
                ('email_status', models.IntegerField(choices=[(1, '已使用'), (0, '未使用')], default=0, verbose_name='邮件状态')),
            ],
            options={
                'verbose_name': '邮件',
                'verbose_name_plural': '邮件',
                'db_table': 'email_recard',
            },
        ),
    ]

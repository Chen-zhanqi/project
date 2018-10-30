# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusermodel',
            name='subject',
            field=models.ManyToManyField(to='subject.SubjectModel', verbose_name='学科'),
        ),
        migrations.AlterField(
            model_name='myusermodel',
            name='role',
            field=models.IntegerField(choices=[(0, '普通用户'), (1, '学科负责人'), (2, '管理员')], default=0),
        ),
    ]

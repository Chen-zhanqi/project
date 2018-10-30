# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-26 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
        ('stage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutlineModel',
            fields=[
                ('publicmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='subject.PublicModel')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('days', models.IntegerField(verbose_name='学时')),
                ('advancing', models.CharField(max_length=255, verbose_name='高级内容')),
                ('remark', models.CharField(max_length=255, verbose_name='备注')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage.StageModel')),
            ],
            options={
                'db_table': 'outline',
            },
            bases=('subject.publicmodel',),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-06-21 04:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_codedic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codedic',
            options={'verbose_name': '数据字典', 'verbose_name_plural': '数据字典'},
        ),
        migrations.RemoveField(
            model_name='codedic',
            name='code',
        ),
    ]
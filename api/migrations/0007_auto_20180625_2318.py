# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-06-25 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180625_2308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='product',
            new_name='product_name',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='series_num',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product_model',
            field=models.CharField(default=1, max_length=100, verbose_name='产品型号'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.FloatField(default=1, verbose_name='价格'),
            preserve_default=False,
        ),
    ]

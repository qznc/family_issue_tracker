# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_auto_20160712_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
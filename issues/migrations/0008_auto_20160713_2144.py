# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_auto_20160712_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='issue',
            name='creator',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]

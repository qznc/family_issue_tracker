# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='issues.Issue'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issue',
            name='closed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
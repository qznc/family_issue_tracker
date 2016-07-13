# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0008_auto_20160713_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='text body'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creator',
            field=models.CharField(blank=True, max_length=256, verbose_name='creator'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='issues.Issue', verbose_name='issue'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='closed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='closed'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='creator',
            field=models.CharField(blank=True, max_length=256, verbose_name='creator'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True, help_text='Editable text field', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='for_anon',
            field=models.BooleanField(default=False, help_text='Anonymous users can see this issue', verbose_name='for anonymous'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='subscriber_only',
            field=models.BooleanField(default=False, help_text='Only subscribers see this issue', verbose_name='subscriber only'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='title',
            field=models.CharField(max_length=60, verbose_name='title'),
        ),
    ]

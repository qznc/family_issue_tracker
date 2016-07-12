# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(help_text='Editable text field')),
                ('created', models.DateTimeField()),
                ('closed', models.DateTimeField()),
                ('for_anon', models.BooleanField(default=False, help_text='Anonymous users can see this issue')),
                ('subscriber_only', models.BooleanField(default=False, help_text='Only subscribers see this issue')),
            ],
        ),
    ]

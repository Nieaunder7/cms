# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20171024_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_device',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_member',
        ),
        migrations.AddField(
            model_name='project',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCaseList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('suite', models.CharField(max_length=50)),
                ('case', models.CharField(max_length=50)),
                ('task', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=50)),
                ('context', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=50)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 13:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0006_auto_20170728_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='duracao_total',
            field=models.DurationField(default=datetime.timedelta(0), null=True),
        ),
    ]

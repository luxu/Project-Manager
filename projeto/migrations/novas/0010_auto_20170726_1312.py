# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0009_auto_20170703_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]

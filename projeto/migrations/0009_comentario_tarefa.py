# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0008_tarefa_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='tarefa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projeto.Tarefa'),
            preserve_default=False,
        ),
    ]

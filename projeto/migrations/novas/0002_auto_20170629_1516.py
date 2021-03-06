# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Participacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participacoes', to='projeto.Equipe')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='funcao',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='pre_requisito',
            field=models.ManyToManyField(related_name='pre_requisitos', to='projeto.Tarefa'),
        ),
        migrations.AddField(
            model_name='participacao',
            name='funcao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projeto.Funcao'),
        ),
        migrations.AddField(
            model_name='participacao',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participacoes', to='projeto.Funcionario'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='membros',
            field=models.ManyToManyField(through='projeto.Participacao', to='projeto.Funcionario'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='projeto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projeto.Projeto'),
        ),
    ]

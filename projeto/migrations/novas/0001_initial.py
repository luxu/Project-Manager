# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('porcentagem_concluida', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projeto.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='projeto.Checklist')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
                ('esforco', models.DurationField()),
                ('data_conclusao', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[(0, 'A fazer'), (1, 'Fazendo'), (2, 'Feito')], max_length=1)),
                ('pre_requisito', models.ManyToManyField(related_name='_tarefa_pre_requisito_+', to='projeto.Tarefa')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='projeto.Projeto')),
            ],
        ),
        migrations.AddField(
            model_name='checklist',
            name='tarefa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklists', to='projeto.Tarefa'),
        ),
    ]

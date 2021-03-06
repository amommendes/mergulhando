# Generated by Django 2.0.7 on 2018-07-10 03:23
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-10 03:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id_aluno', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('observacoes', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Celula',
            fields=[
                ('id_celula', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('lider', models.CharField(default='Mohamed', max_length=100)),
                ('bairro', models.CharField(default='BDN Tapuapé', max_length=100)),
                ('contato', models.CharField(default='s/ contato', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=600)),
                ('data_ini', models.DateField()),
                ('data_fim', models.DateField()),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id_modulo', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alunos.Cursos')),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id_modulo', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('data', models.DateField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.Alunos')),
                ('modulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alunos.Modulo')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id_turma', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('data_ini', models.DateField()),
                ('data_fim', models.DateField()),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alunos.Cursos')),
            ],
        ),
        migrations.AddField(
            model_name='alunos',
            name='celula',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.SET_DEFAULT, to='alunos.Celula'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-10 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0004_auto_20180709_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.Modulo'),
        ),
    ]

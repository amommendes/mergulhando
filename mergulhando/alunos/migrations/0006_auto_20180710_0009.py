# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-10 00:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0005_auto_20180710_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presenca',
            old_name='curso',
            new_name='modulo',
        ),
    ]
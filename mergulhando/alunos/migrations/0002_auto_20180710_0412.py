# Generated by Django 2.0.7 on 2018-07-10 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='observacoes',
            field=models.CharField(max_length=300, null=True),
        ),
    ]

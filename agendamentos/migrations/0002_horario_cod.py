# Generated by Django 3.2 on 2022-07-06 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='cod',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]

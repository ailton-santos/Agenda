# Generated by Django 4.0.5 on 2022-06-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='user',
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_ag',
            field=models.DateTimeField(blank=True, null=True, verbose_name='data/hora'),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]

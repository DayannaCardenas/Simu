# Generated by Django 2.2.14 on 2022-12-11 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bancoPregunta', '0004_respuesta_resultado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuesta',
            old_name='resultado',
            new_name='respuesta',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='nombre',
        ),
    ]

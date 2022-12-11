# Generated by Django 2.2.14 on 2022-12-10 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('states', '0001_initial'),
        ('bancoPregunta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grado', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_materia', models.CharField(blank=True, max_length=45, null=True)),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='states.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha_aplicacion', models.DateTimeField()),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='states.Estado')),
                ('grado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Grado')),
                ('materia', models.ManyToManyField(to='prueba.Materia')),
                ('prueba_banco', models.ManyToManyField(to='bancoPregunta.BancoPregunta')),
                ('resultado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bancoPregunta.Resultado')),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Materia')),
                ('prueba', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Prueba')),
            ],
        ),
    ]

# Generated by Django 2.2.14 on 2022-12-10 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('states', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('numero_documento', models.CharField(max_length=45)),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='states.Estado')),
                ('tipo_documento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.TipoDocumento')),
            ],
        ),
    ]
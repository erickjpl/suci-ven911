# Generated by Django 5.1.1 on 2024-09-16 00:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('estatus', models.CharField(blank=True, max_length=50, null=True)),
                ('ente', models.CharField(blank=True, max_length=50, null=True)),
                ('nombres_d', models.CharField(max_length=50, verbose_name='Nombre del denunciante')),
                ('apellidos_d', models.CharField(max_length=50, verbose_name='Apellido del denunciante')),
                ('cedula_d', models.CharField(max_length=50, verbose_name='Cédula del denunciante')),
                ('telefono', models.CharField(max_length=11, verbose_name='Teléfono del denunciante')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico')),
                ('direccion_d', models.CharField(max_length=150, verbose_name='Dirección')),
                ('nombres_denunciado', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del denunciado')),
                ('apellidos_denunciado', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido del denunciado')),
                ('cedula_denunciado', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cédula del denunciado')),
                ('motivo', models.CharField(max_length=400)),
                ('zona', models.CharField(blank=True, max_length=150, null=True, verbose_name='Zona del incidente')),
                ('fecha_denuncia', models.DateField(verbose_name='Fecha de la denuncia')),
                ('fecha_incidente', models.DateField(blank=True, null=True, verbose_name='Fecha del incidente')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'denuncia',
                'verbose_name_plural': 'denuncias',
            },
        ),
    ]

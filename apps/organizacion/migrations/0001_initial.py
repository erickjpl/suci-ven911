# Generated by Django 5.1.1 on 2024-11-23 23:23

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
            name='Normativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Nombre de Normativa:')),
                ('file', models.FileField(default='', upload_to='normativas/', verbose_name='Archivo')),
                ('user', models.CharField(default='', max_length=64, verbose_name='Usuario')),
                ('date', models.DateField(blank=True, verbose_name='Fecha')),
                ('progre', models.CharField(default='', max_length=64, verbose_name='Progreso:')),
                ('estado', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'normativa',
                'verbose_name_plural': 'normativas',
            },
        ),
        migrations.CreateModel(
            name='Reglamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Nombre de Reglamento:')),
                ('file', models.FileField(default='', upload_to='reglamentos/', verbose_name='Archivo')),
                ('user', models.CharField(default='', max_length=64, verbose_name='Usuario')),
                ('date', models.DateField(blank=True, verbose_name='Fecha')),
                ('progre', models.CharField(default='', max_length=64, verbose_name='Progreso:')),
                ('estado', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'reglamento',
                'verbose_name_plural': 'reglamentos',
            },
        ),
    ]
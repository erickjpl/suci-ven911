# Generated by Django 5.1.1 on 2024-11-23 22:29

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
            name='CuadrantePaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('nombre', models.CharField(max_length=180)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'cuadrante de paz',
                'verbose_name_plural': 'cuadrantes de paz',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('departamento', models.CharField(max_length=90)),
                ('estatus', models.CharField(choices=[('act', 'Activo'), ('ina', 'Inactivo'), ('cer', 'Cerrado')], max_length=3)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('sede', models.CharField(max_length=30)),
                ('estatus', models.CharField(choices=[('act', 'Activo'), ('rem', 'Remodelacion'), ('cer', 'Cerrada')], max_length=3)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'sede',
                'verbose_name_plural': 'sedes',
            },
        ),
        migrations.CreateModel(
            name='Bien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('nombre', models.CharField(max_length=60)),
                ('marca', models.CharField(blank=True, max_length=90, null=True, verbose_name='Marca:')),
                ('modelo', models.CharField(blank=True, max_length=90, null=True, verbose_name='Modelo:')),
                ('serial', models.CharField(blank=True, max_length=90, null=True, verbose_name='Serial:')),
                ('descripcion', models.TextField(blank=True, max_length=120, null=True, verbose_name='Descripción:')),
                ('cantidad', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_adquirido', models.DateField(verbose_name='Fecha de adquisición')),
                ('condicion', models.CharField(choices=[('nuevo', 'Nuevo'), ('usado', 'Usado')], max_length=5, verbose_name='Condición')),
                ('garantia', models.DateField(blank=True, max_length=60, null=True, verbose_name='Garantía')),
                ('estatus', models.CharField(choices=[('act', 'Activo'), ('ina', 'Inactivo')], max_length=3)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.departamento')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.sede')),
            ],
            options={
                'verbose_name': 'bien',
                'verbose_name_plural': 'bienes',
            },
        ),
    ]

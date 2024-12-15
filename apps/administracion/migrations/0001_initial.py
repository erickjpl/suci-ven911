# Generated by Django 5.1.1 on 2024-12-15 14:11

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
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('descripcion', models.TextField(max_length=255)),
                ('marca', models.CharField(blank=True, max_length=255, null=True)),
                ('modelo', models.CharField(blank=True, max_length=255, null=True)),
                ('serial', models.CharField(blank=True, max_length=255, null=True)),
                ('placa', models.CharField(blank=True, max_length=255, null=True)),
                ('cantidad_combustible', models.IntegerField(blank=True, null=True)),
                ('codigo_bn', models.CharField(blank=True, max_length=255, null=True)),
                ('cantidad', models.IntegerField()),
                ('condicion', models.CharField(choices=[('N', 'Nuevo'), ('U', 'Usado'), ('D', 'Deteriorado')], max_length=1)),
                ('fecha_adq', models.DateField()),
                ('asignado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Actividad social',
                'verbose_name_plural': 'Actividades sociales',
                'db_table': 'administracion_articulos',
                'ordering': ['-id'],
                'permissions': [('listar_articulo', 'Puede listar articulos'), ('agregar_articulo', 'Puede agregar articulo'), ('ver_articulo', 'Puede ver articulo'), ('editar_articulo', 'Puede actualizar articulo'), ('eliminar_articulo', 'Puede eliminar articulo')],
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('sede', models.CharField(max_length=30)),
                ('estatus', models.CharField(choices=[('act', 'Activo'), ('rem', 'Remodelacion'), ('cer', 'Cerrada')], max_length=3)),
            ],
            options={
                'verbose_name': 'sede',
                'verbose_name_plural': 'sedes',
            },
        ),
        migrations.CreateModel(
            name='TipoArticulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('nombre', models.CharField(max_length=180)),
            ],
            options={
                'verbose_name': 'Tipo de Articulo',
                'verbose_name_plural': 'Tipos de Articulos',
                'db_table': 'administracion_tipos_articulos',
                'ordering': ['-id'],
                'permissions': [('listar_type_articulo', 'Puede listar tipos de articulos'), ('agregar_type_articulo', 'Puede agregar tipo de articulo'), ('ver_type_articulo', 'Puede ver tipo de articulo'), ('editar_type_articulo', 'Puede actualizar tipo de articulo'), ('eliminar_type_articulo', 'Puede eliminar tipo de articulo')],
            },
        ),
        migrations.CreateModel(
            name='TipoAveria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('n_orden', models.IntegerField()),
                ('valor_bs', models.IntegerField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.articulo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField(max_length=255)),
                ('observaciones', models.TextField(max_length=255)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.articulo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.departamento')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.sede')),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignaciones',
                'db_table': 'administracion_asignacion',
                'ordering': ['-id'],
                'permissions': [('listar_asignacion', 'Puede listar asignacions'), ('agregar_asignacion', 'Puede agregar asignacion'), ('ver_asignacion', 'Puede ver asignacion'), ('editar_asignacion', 'Puede actualizar asignacion'), ('eliminar_asignacion', 'Puede eliminar asignacion')],
            },
        ),
        migrations.AddField(
            model_name='articulo',
            name='tipo_articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.tipoarticulo'),
        ),
        migrations.CreateModel(
            name='Averia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('problema', models.TextField(max_length=255)),
                ('ubicacion', models.TextField(max_length=255)),
                ('serial', models.CharField(max_length=255)),
                ('codigo_bn', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.departamento')),
                ('tipo_averia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.tipoaveria')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 5.1.1 on 2025-01-25 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoIncidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('tipo', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('estado', models.CharField(choices=[('1', 'Amazonas'), ('2', 'Anzoátegui'), ('3', 'Apure'), ('4', 'Aragua'), ('5', 'Barinas'), ('6', 'Bolívar'), ('7', 'Carabobo'), ('8', 'Cojedes'), ('9', 'Delta Amacuro'), ('10', 'Falcón'), ('11', 'Guárico'), ('12', 'Lara'), ('13', 'Mérida'), ('14', 'Miranda'), ('15', 'Monagas'), ('16', 'Nueva Esparta'), ('17', 'Portuguesa'), ('18', 'Sucre'), ('19', 'Táchira'), ('20', 'Trujillo'), ('21', 'Vargas'), ('22', 'Yaracuy'), ('23', 'Zulia'), ('24', 'Distrito Capital')], max_length=2, verbose_name='Estado')),
                ('tipo_solicitud', models.CharField(max_length=80, verbose_name='Tipo Solicitud')),
                ('observaciones', models.CharField(max_length=200)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.departamento')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.sede')),
                ('tipo_incidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='potencia.tipoincidencia')),
            ],
            options={
                'verbose_name': 'Incidencia',
                'verbose_name_plural': 'Incidencias',
            },
        ),
    ]

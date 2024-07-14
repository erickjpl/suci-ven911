# Generated by Django 5.0.3 on 2024-04-03 22:09

import django.db.models.deletion
import django.utils.timezone
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
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrganismoCompetente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencia.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('id_cuadrante_paz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencia.cuadrantepaz')),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencia.estado')),
                ('id_municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencia.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denunciante', models.CharField(max_length=255)),
                ('telefono_denunciante', models.CharField(blank=True, max_length=255)),
                ('direccion_incidencia', models.TextField(blank=True)),
                ('observaciones', models.TextField(blank=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencia.estado')),
                ('id_incidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencia.incidencia')),
                ('id_municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencia.municipio')),
                ('id_organismo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencia.organismocompetente')),
                ('id_parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencia.parroquia')),
            ],
        ),
    ]

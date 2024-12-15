# Generated by Django 5.1.1 on 2024-12-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Normativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Nombre de Normativa:')),
                ('file', models.FileField(default='', upload_to='normativas/', verbose_name='Archivo')),
                ('user', models.CharField(default='', max_length=64, verbose_name='Usuario')),
                ('date', models.DateField(blank=True, verbose_name='Fecha')),
                ('progre', models.CharField(default='', max_length=64, verbose_name='Progreso:')),
                ('estado', models.BooleanField(default=False)),
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
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Nombre de Reglamento:')),
                ('file', models.FileField(default='', upload_to='reglamentos/', verbose_name='Archivo')),
                ('user', models.CharField(default='', max_length=64, verbose_name='Usuario')),
                ('date', models.DateField(blank=True, verbose_name='Fecha')),
                ('progre', models.CharField(default='', max_length=64, verbose_name='Progreso:')),
                ('estado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'reglamento',
                'verbose_name_plural': 'reglamentos',
            },
        ),
    ]

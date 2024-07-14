# Generated by Django 5.0.1 on 2024-06-16 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0005_remove_ambulancia_transporte_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=64, verbose_name='Nombre:')),
                ('apellido', models.CharField(default='', max_length=64, verbose_name='Apellido:')),
                ('cedula', models.CharField(default='', max_length=64, verbose_name='Cédula:')),
                ('modelo', models.CharField(default='', max_length=64, verbose_name='Modelo:')),
                ('vehiculo', models.CharField(default='', max_length=64, verbose_name='Tipo de vehiculo:')),
                ('motivo', models.CharField(default='', max_length=64, verbose_name='Motivo:')),
                ('capagasolina', models.CharField(default='', max_length=64, verbose_name='Capacidad de Gasolina:')),
                ('cantigasolina', models.CharField(default='', max_length=64, verbose_name='Capacidad de Gasolina:')),
                ('placa', models.CharField(default='', max_length=64, verbose_name='Placa:')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.CharField(default='', max_length=64, verbose_name='Hora:')),
            ],
        ),
        migrations.DeleteModel(
            name='Ambulancia',
        ),
        migrations.DeleteModel(
            name='Particular',
        ),
        migrations.DeleteModel(
            name='Patrulla',
        ),
    ]

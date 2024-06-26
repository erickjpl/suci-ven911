# Generated by Django 5.0.3 on 2024-04-03 22:09

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
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'cargo',
                'verbose_name_plural': 'cargos',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_civil', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'estado_civil',
                'verbose_name_plural': 'estados_civiles',
            },
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado_instruccion', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'grado_instruccion',
                'verbose_name_plural': 'grados_instruccion',
            },
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nacionalidad', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'nacionalidad',
                'verbose_name_plural': 'nacionalidades',
            },
        ),
        migrations.CreateModel(
            name='Sangre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_sangre', models.CharField(max_length=9)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'tipo_sangre',
                'verbose_name_plural': 'tipos_sangre',
            },
        ),
        migrations.CreateModel(
            name='Sedes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sede', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'sede',
                'verbose_name_plural': 'sedes',
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=9)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'sexo',
                'verbose_name_plural': 'sexos',
            },
        ),
        migrations.CreateModel(
            name='TallasCamisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla_camisa', models.CharField(max_length=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'talla_camisa',
                'verbose_name_plural': 'tallas_camisas',
            },
        ),
        migrations.CreateModel(
            name='TallasPantalon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla_pantalon', models.CharField(max_length=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'talla_pantalon',
                'verbose_name_plural': 'tallas_pantalones',
            },
        ),
        migrations.CreateModel(
            name='TallasZapatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla_zapato', models.CharField(max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'talla_zapato',
                'verbose_name_plural': 'tallas_zapatos',
            },
        ),
        migrations.CreateModel(
            name='TipoPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_personal', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'tipo_personal',
                'verbose_name_plural': 'tipos_personales',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(blank=True, max_length=50, null=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula', models.IntegerField()),
                ('fecha_nac', models.DateField()),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=11)),
                ('conyugue', models.CharField(blank=True, max_length=50, null=True)),
                ('cedula_conyugue', models.IntegerField(blank=True, null=True)),
                ('discapacitado', models.BooleanField()),
                ('direccion', models.CharField(max_length=150)),
                ('nro_cuenta', models.CharField(max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('estudias', models.BooleanField()),
                ('comision_servicio', models.BooleanField()),
                ('pnb', models.BooleanField()),
                ('fecha_ingreso_911', models.DateField()),
                ('fecha_ingreso_apn', models.DateField()),
                ('contratos', models.IntegerField()),
                ('niño_menor_12', models.IntegerField(blank=True, null=True)),
                ('edades1', models.IntegerField(blank=True, null=True)),
                ('hijos_13_18', models.IntegerField(blank=True, null=True)),
                ('edades2', models.IntegerField(blank=True, null=True)),
                ('niña_menor_12', models.IntegerField(blank=True, null=True)),
                ('edades3', models.IntegerField(blank=True, null=True)),
                ('hijos_discapacidad', models.IntegerField(blank=True, null=True)),
                ('edades4', models.IntegerField(blank=True, null=True)),
                ('motivo', models.CharField(blank=True, max_length=50, null=True)),
                ('fasmij', models.BooleanField()),
                ('parentezco1', models.CharField(blank=True, max_length=10, null=True)),
                ('beneficiario1', models.CharField(blank=True, max_length=50, null=True)),
                ('cedula1', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion1', models.CharField(blank=True, max_length=150, null=True)),
                ('parentezco2', models.CharField(blank=True, max_length=10, null=True)),
                ('beneficiario2', models.CharField(blank=True, max_length=50, null=True)),
                ('cedula2', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion2', models.CharField(blank=True, max_length=150, null=True)),
                ('parentezco3', models.CharField(blank=True, max_length=10, null=True)),
                ('beneficiario3', models.CharField(blank=True, max_length=50, null=True)),
                ('cedula3', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion3', models.CharField(blank=True, max_length=150, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.cargo')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.departamento')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.estadocivil')),
                ('grado_instruccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.grado')),
                ('nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.nacionalidad')),
                ('tipo_sangre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.sangre')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.sedes')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.sexo')),
                ('talla_camisa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.tallascamisa')),
                ('talla_pantalon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.tallaspantalon')),
                ('talla_zapato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.tallaszapatos')),
                ('tipo_personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.tipopersonal')),
            ],
            options={
                'verbose_name': 'personal',
                'verbose_name_plural': 'personales',
            },
        ),
    ]

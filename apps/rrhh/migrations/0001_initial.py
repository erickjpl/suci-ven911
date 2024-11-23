# Generated by Django 5.1.1 on 2024-11-23 23:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('cargo', models.CharField(max_length=60)),
                ('estatus', models.CharField(choices=[('act', 'Activo'), ('ina', 'Inactivo'), ('inv', 'Invalido'), ('cer', 'Cerrado')], max_length=3)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'cargo',
                'verbose_name_plural': 'cargos',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('estatus', models.CharField(choices=[('act', 'Activo'), ('vac', 'En vacaciones'), ('sus', 'Suspendido'), ('des', 'Se despedio'), ('ren', 'Ha renunciado')], max_length=3)),
                ('nombres', models.CharField(max_length=90)),
                ('apellidos', models.CharField(max_length=90)),
                ('nacionalidad', models.CharField(choices=[('ve', 'Venezolano'), ('ex', 'Extranjero')], max_length=2)),
                ('cedula', models.IntegerField()),
                ('sexo', models.CharField(choices=[('f', 'Femenino'), ('m', 'Masculino')], max_length=1)),
                ('fecha_nacimiento', models.DateField()),
                ('estado_civil', models.CharField(choices=[('s', 'Soltero'), ('c', 'Casado'), ('d', 'Divorviado'), ('v', 'Viudo')], max_length=1)),
                ('tipo_sangre', models.CharField(choices=[('a+', 'A+ (Rh positivo)'), ('a-', 'A- (Rh negativo)'), ('b+', 'B+ (Rh positivo)'), ('b-', 'B- (Rh negativo)'), ('ab+', 'AB+ (Rh positivo)'), ('ab-', 'AB- (Rh negativo)'), ('o+', 'O+ (Rh positivo)'), ('o-', 'O- (Rh negativo)')], max_length=3)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=180)),
                ('estudia', models.BooleanField()),
                ('discapacitado', models.BooleanField()),
                ('contratos', models.IntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
            },
        ),
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('colegio', models.CharField(max_length=120)),
                ('codigo_titulo', models.CharField(max_length=120)),
                ('titulo', models.CharField(max_length=120)),
                ('area_conocimiento', models.CharField(max_length=120)),
                ('fecha_inicio', models.DateField()),
                ('fecha_culminacion', models.DateField()),
                ('enlace_certificado', models.CharField(blank=True, max_length=120, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.empleado')),
            ],
            options={
                'verbose_name': 'educacion',
                'verbose_name_plural': 'educaciones',
            },
        ),
        migrations.CreateModel(
            name='Dotacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('camisa', models.CharField(choices=[('XS', 'Extra Pequena'), ('S', 'Pequena'), ('M', 'Mediana'), ('L', 'Grande'), ('XL', 'Extra Grande')], max_length=2)),
                ('pantalon', models.CharField(choices=[('8', 'Extra Pequena (Dama)'), ('10', 'Pequena (Dama)'), ('12', 'Mediana (Dama)'), ('14', 'Grande (Dama)'), ('16', 'Extra Grande (Dama)'), ('18', 'Super Grande (Dama)'), ('20', 'Gigante (Dama)'), ('28', 'Extra Pequena (Caballero)'), ('30', 'Pequena (Caballero)'), ('32', 'Mediana (Caballero)'), ('34', 'Grande (Caballero)'), ('36', 'Extra Grande (Caballero)'), ('38', 'Super Grande (Caballero)'), ('40', 'Gigante (Caballero)'), ('42', 'Extra Gigante (Caballero)')], max_length=2)),
                ('zapato', models.CharField(choices=[('33', 'Talla 33'), ('34', 'Talla 34'), ('35', 'Talla 35'), ('36', 'Talla 36'), ('37', 'Talla 37'), ('38', 'Talla 38'), ('39', 'Talla 39'), ('40', 'Talla 40'), ('41', 'Talla 41'), ('42', 'Talla 42'), ('43', 'Talla 43'), ('44', 'Talla 44'), ('45', 'Talla 45'), ('46', 'Talla 46')], max_length=2)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.empleado')),
            ],
            options={
                'verbose_name': 'dotacion',
                'verbose_name_plural': 'dotaciones',
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('banco', models.CharField(choices=[('0001', '0001 - Banco Central de Venezuela'), ('0102', '0102 - Banco de Venezuela'), ('0104', '0104 - Banco Venezolano de Crédito'), ('0105', '0105 - Mercantil Banco'), ('0108', '0108 - BBVA Provincial'), ('0114', '0114 - Bancaribe'), ('0115', '0115 - Banco Exterior'), ('0116', '0116 - Banco Occidental de Descuento'), ('0128', '0128 - Banco Caroní'), ('0134', '0134 - Banesco'), ('0137', '0137 - Banco Sofitasa'), ('0138', '0138 - Banco Plaza'), ('0146', '0146 - Banco de la Gente Emprendedora'), ('0151', '0151 - Banco Fondo Común'), ('0156', '0156 - 100% Banco'), ('0157', '0157 - DelSur'), ('0163', '0163 - Banco del Tesoro'), ('0166', '0166 - Banco Agrícola de Venezuela'), ('0168', '0168 - Bancrecer'), ('0169', '0169 - Mi Banco'), ('0171', '0171 - Banco Activo'), ('0172', '0172 - Bancamiga'), ('0173', '0173 - Banco Internacional de Desarrollo'), ('0174', '0174 - Banplus'), ('0175', '0175 - Banco Bicentenario'), ('0177', '0177 - Banco de la Fuerza Armada Nacional Bolivariana'), ('0178', '0178 - N58 Banco Digital'), ('0190', '0190 - Citibank'), ('0191', '0191 - Banco Nacional de Crédito'), ('0601', '0601 - Instituto Municipal de Crédito Popular')], max_length=4)),
                ('tipo', models.CharField(choices=[('cor', 'Cuenta Corriente'), ('aho', 'Cuenta de Ahorros')], max_length=3)),
                ('numero_cuenta', models.CharField(max_length=30)),
                ('cedula', models.IntegerField()),
                ('pago_movil', models.BooleanField()),
                ('telefono', models.CharField(max_length=12)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.empleado')),
            ],
            options={
                'verbose_name': 'cuenta',
                'verbose_name_plural': 'cuentas',
            },
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('parentezco', models.CharField(choices=[('hermano', 'Hermana|Hermano'), ('pareja', 'Conyugue'), ('mama', 'Madre'), ('papa', 'Padre'), ('hijo', 'Hija|Hijo')], max_length=7)),
                ('tipo_hijo', models.CharField(blank=True, choices=[('menor_12', 'Hijo menor de 12'), ('hijos_13_18', 'Hijo entre 13 y 18'), ('mayor_18', 'Hijo mayor de 18')], max_length=11, null=True)),
                ('discapacidad', models.BooleanField(default=False)),
                ('nombres', models.CharField(max_length=90)),
                ('apellidos', models.CharField(max_length=90)),
                ('cedula', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('f', 'Femenino'), ('m', 'Masculino')], max_length=1)),
                ('estado_civil', models.CharField(choices=[('s', 'Soltero'), ('c', 'Casado'), ('d', 'Divorviado'), ('v', 'Viudo')], max_length=1)),
                ('observacion', models.CharField(blank=True, max_length=150, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.empleado')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'familiar',
                'verbose_name_plural': 'familiares',
            },
        ),
        migrations.CreateModel(
            name='Sueldo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('estatus', models.CharField(choices=[('pendiente', 'Por Pagar'), ('pagado', 'Pago completado'), ('suspendido', 'Suspendido')], max_length=10)),
                ('fecha_pago', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.empleado')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'sueldo',
                'verbose_name_plural': 'sueldos',
            },
        ),
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('tipo_personal', models.CharField(max_length=60)),
                ('estatus', models.CharField(choices=[('act', 'Activo'), ('ina', 'Inactivo'), ('inv', 'Invalido'), ('cer', 'Cerrado')], max_length=3)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'tipo de empleado',
                'verbose_name_plural': 'tipos de empleados',
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('tipo', models.CharField(choices=[('pasante', 'Pasante'), ('prueba', 'Periodo de Prueba'), ('contrato', 'Contratado'), ('fijo', 'Personal Fijo')], max_length=8)),
                ('comision_servicio', models.BooleanField()),
                ('pnb', models.BooleanField()),
                ('fecha_ingreso_911', models.DateField()),
                ('fecha_ingreso_apn', models.DateField()),
                ('fasmij', models.BooleanField()),
                ('fecha_ingreso', models.DateField()),
                ('fecha_culminacion', models.DateField(blank=True, null=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.cargo')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.departamento')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.sede')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.empleado')),
                ('tipo_personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.tipoempleado')),
            ],
            options={
                'verbose_name': 'contrato',
                'verbose_name_plural': 'contratos',
            },
        ),
        migrations.CreateModel(
            name='TipoSueldo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('tipo', models.CharField(choices=[('ticket', 'Cesta Ticket'), ('guerra', 'Bono de Guerra'), ('discapacidad', 'Prima por discapacidad'), ('menor_12', 'Prima por dependecias menores de 12'), ('hijos_13_18', 'Prima por dependecias menores de 13 a 18'), ('hijos_discapacidad', 'Prima por dependecias menores con discapacidad'), ('profesionalismo', 'Prima por Profesionalismo'), ('minimo', 'Sueldo Minimo')], max_length=21)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('estatus', models.CharField(choices=[('act', 'Activo'), ('sup', 'Suspendido'), ('des', 'Desactivado')], max_length=3)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'tipo de empleado',
                'verbose_name_plural': 'tipos de empleados',
            },
        ),
        migrations.CreateModel(
            name='SueldoDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted', models.BooleanField(default=False, verbose_name='Está eliminado')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('fecha_pago', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_delete', to=settings.AUTH_USER_MODEL, verbose_name='Eliminado por')),
                ('sueldo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.sueldo')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
                ('tipo_sueldo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.tiposueldo')),
            ],
            options={
                'verbose_name': 'detalles del sueldo',
                'verbose_name_plural': 'destalles de los sueldos',
            },
        ),
    ]

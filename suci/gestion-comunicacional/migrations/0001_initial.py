# Generated by Django 5.0.1 on 2024-05-30 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Equipo')),
                ('description', models.TextField(verbose_name='Descripción del equipo')),
                ('status', models.CharField(choices=[('available', 'Available'), ('loaned', 'Loaned'), ('maintenance', 'Maintenance')], max_length=50, verbose_name='Estatus del equipo')),
            ],
        ),
        migrations.CreateModel(
            name='SocialActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('workshop', 'Workshop'), ('conference', 'Conference'), ('campaign', 'Campaign')], max_length=50, verbose_name='Tipo de actividad')),
                ('date', models.DateField(verbose_name='Fecha de la actividad')),
                ('location', models.CharField(max_length=255, verbose_name='Lugar de la actividad')),
                ('description', models.TextField(verbose_name='Descripcion de la actividad')),
                ('reason', models.TextField(verbose_name='Motivo para realizar la actividad')),
                ('beneficiaries', models.IntegerField(verbose_name='Cantidad de personas beneficiadas')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Twitter', 'Twitter')], max_length=50, verbose_name='Plataforma')),
                ('username', models.CharField(max_length=60, verbose_name='Nombre de usuario')),
                ('url', models.URLField(verbose_name='Direccion web')),
                ('followers', models.PositiveSmallIntegerField(verbose_name='Seguidores')),
                ('responsible', models.CharField(max_length=100, verbose_name='Quien administra la red')),
                ('publications', models.PositiveSmallIntegerField(verbose_name='Publicaciones')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100, verbose_name='Departamento')),
                ('loan_date', models.DateField(verbose_name='Fecha del préstamo')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='Fecha de devolución')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gc.equipment', verbose_name='Equipo ID')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('reel', 'Reel'), ('post', 'Post'), ('story', 'Story'), ('picture', 'Picture')], max_length=50, verbose_name='Tipo de publicacion')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('publish_date', models.DateField(verbose_name='Fecha de publicacion')),
                ('status', models.CharField(choices=[('published', 'Published'), ('scheduled', 'Scheduled'), ('draft', 'Draft')], max_length=50, verbose_name='Estatus')),
                ('reach', models.IntegerField(verbose_name='Alcance de la publicación')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gc.socialmediaaccount', verbose_name='Cuenta')),
            ],
        ),
    ]
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

#BASE DE DATOS DEL MODULO SEGURIDAD INTEGRAL - ENTRADA
class Entradap(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido:', default='')
    cedula = models.CharField(max_length=64, verbose_name='Cédula:', default='')
    telefono = models.CharField(max_length=64, verbose_name='Teléfono:', default='')
    fecha = models.DateField(verbose_name='Fecha')
    direccion = models.CharField(max_length=64, verbose_name='Dirección:', default='')
    cargo = models.CharField(max_length=64, verbose_name='Cargo:', default='')
    hora = models.CharField(max_length=64, verbose_name='Hora de Entrada:', default='')

#BASE DE DATOS DEL MODULO SEGURIDAD INTEGRAL - SALIDA
class Salidap(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido:', default='')
    cedula = models.CharField(max_length=64, verbose_name='Cédula:', default='')
    telefono = models.CharField(max_length=64, verbose_name='Teléfono:', default='')
    fecha = models.DateField(verbose_name='Fecha')
    direccion = models.CharField(max_length=64, verbose_name='Dirección:', default='')
    cargo = models.CharField(max_length=64, verbose_name='Cargo:', default='')
    hora = models.CharField(max_length=64, verbose_name='Hora de Entrada:', default='')

#BASE DE DATOS DEL MODULO SEGURIDAD INTEGRAL - GESTION
class Gestion(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido:', default='')
    cedula = models.CharField(max_length=64, verbose_name='Cédula:', default='')
    tipo = models.CharField(max_length=64, verbose_name='Tipo de Incidente:', default='')
    descripcion = models.CharField(max_length=64, verbose_name='Descripción:', default='')
    fecha = models.DateField(verbose_name='Fecha')
    direccion = models.CharField(max_length=64, verbose_name='Dirección:', default='')
    cargo = models.CharField(max_length=64, verbose_name='Cargo:', default='')
    hora = models.CharField(max_length=64, verbose_name='Hora de Entrada:', default='')

#BASE DE DATOS DEL MODULO - VEHICULOS
class Vehiculos(models.Model):
    nombre = models.CharField(max_length=64, verbose_name='Nombre:', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido:', default='')
    cedula = models.CharField(max_length=64, verbose_name='Cédula:', default='')
    modelo = models.CharField(max_length=64, verbose_name='Modelo:', default='')
    vehiculo = models.CharField(max_length=64, verbose_name='Tipo de vehiculo:', default='')
    motivo = models.CharField(max_length=64, verbose_name='Motivo:', default='')
    capagasolina = models.CharField(max_length=64, verbose_name='Capacidad de Gasolina:', default='')
    cantigasolina = models.CharField(max_length=64, verbose_name='Capacidad de Gasolina:', default='')
    placa = models.CharField(max_length=64, verbose_name='Placa:', default='')
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.CharField(max_length=64, verbose_name='Hora:', default='')
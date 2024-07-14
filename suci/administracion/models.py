from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

#BASE DE DATOS DE BIENES
class Bienes(models.Model):
    descripcion = models.TextField(max_length=64, verbose_name='Descripción:', default='')
    marca = models.CharField(max_length=64, verbose_name='Marca:', default='')
    modelo = models.CharField(max_length=64, verbose_name='Modelo:', default='')
    serial = models.CharField(max_length=64, verbose_name='Serial:', default='')
    cantidad = models.CharField(max_length=64, verbose_name='Cantidad:', default='')
    asignado = models.CharField(max_length=64, verbose_name='Asignado:', default='')
    valor = models.CharField(max_length=64, verbose_name='Valor:', default='')
    condicion = models.CharField(max_length=64, verbose_name='Condición:', default='')
    ubicacion = models.CharField(max_length=64, verbose_name='Ubicación:', default='')
    fecha_adq = models.DateField(verbose_name='Fecha')
    garantia = models.CharField(max_length=64, verbose_name='Garantía:', default='')

#BASE DE DATOS DE CONSUMIBLE
class Consumible(models.Model):
    descripcion = models.TextField(max_length=64, verbose_name='Descripción:', default='')
    marca = models.CharField(max_length=64, verbose_name='Marca:', default='')
    serial = models.CharField(max_length=64, verbose_name='Serial:', default='')
    cantidad = models.CharField(max_length=64, verbose_name='Cantidad:', default='')
    valor = models.CharField(max_length=64, verbose_name='Valor:', default='')
    condicion = models.CharField(max_length=64, verbose_name='Condición:', default='')
    ubicacion = models.CharField(max_length=64, verbose_name='Ubicación:', default='')
    fecha_adq = models.DateField(verbose_name='Fecha')
    observaciones = models.TextField(max_length=64, verbose_name='Observaciones:', default='')

#BASE DE DATOS DE MOBILIARIO
class Mobiliario(models.Model):
    descripcion = models.TextField(max_length=64, verbose_name='Descripción:', default='')
    marca = models.CharField(max_length=64, verbose_name='Marca:', default='')
    serial = models.CharField(max_length=64, verbose_name='Serial:', default='')
    cantidad = models.CharField(max_length=64, verbose_name='Cantidad:', default='')
    valor = models.CharField(max_length=64, verbose_name='Valor:', default='')
    condicion = models.CharField(max_length=64, verbose_name='Condición:', default='')
    ubicacion = models.CharField(max_length=64, verbose_name='Ubicación:', default='')
    fecha_adq = models.DateField(verbose_name='Fecha')
    garantia = models.CharField(max_length=64, verbose_name='Garantía:', default='')
    observaciones = models.TextField(max_length=64, verbose_name='Observaciones:', default='')
    codigo_bn = models.CharField(max_length=64, verbose_name='Código BN:', default='')

#BASE DE DATOS DE AVERIA
class Averia(models.Model):
    bienes = models.TextField(max_length=64, verbose_name='Bienes:', default='')
    sintomas = models.CharField(max_length=64, verbose_name='Sintomas:', default='')
    departamento_ave = models.CharField(max_length=64, verbose_name='Departamento:', default='')
    problema = models.CharField(max_length=64, verbose_name='Problema:', default='')
    condicion = models.CharField(max_length=64, verbose_name='Condición:', default='')
    ubicacion = models.CharField(max_length=64, verbose_name='Ubicación:', default='')
    codigo_bn = models.CharField(max_length=64, verbose_name='Código BN:', default='')

#BASE DE DATOS DE COMPRAS
class Compras(models.Model):
    producto = models.TextField(max_length=64, verbose_name='Producto:', default='')
    serial = models.CharField(max_length=64, verbose_name='Serial:', default='')
    marca = models.CharField(max_length=64, verbose_name='Marca:', default='')
    modelo = models.CharField(max_length=64, verbose_name='Modelo:', default='')
    fecha_adq = models.DateField(verbose_name='Fecha')
    numero_orden = models.CharField(max_length=64, verbose_name='Número de orden:', default='')
    valor = models.CharField(max_length=64, verbose_name='Valor:', default='')
    cantidad = models.CharField(max_length=64, verbose_name='Cantidad:', default='')
    proveedor = models.CharField(max_length=64, verbose_name='Proveedor:', default='')
    ubicacion = models.CharField(max_length=64, verbose_name='Ubicación:', default='')
    garantia = models.CharField(max_length=64, verbose_name='Garantía:', default='')

#BASE DE DATOS DE COMPRAS
class Asignacion(models.Model):
    inventario = models.CharField(max_length=64, verbose_name='Inventario:', default='')
    departamento = models.CharField(max_length=64, verbose_name='Departamento:', default='')
    descripcion = models.CharField(max_length=64, verbose_name='Descripción:', default='')
    articulo = models.CharField(max_length=64, verbose_name='Articulo:', default='')
    cantidad = models.CharField(max_length=64, verbose_name='Cantidad:', default='')
    observaciones = models.CharField(max_length=64, verbose_name='Observaciones:', default='')
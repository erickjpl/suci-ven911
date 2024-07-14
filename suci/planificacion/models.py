from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

#BASE DE DATOS DEL MODULO PLANIFICACION
class Objetivos(models.Model):
    fechai = models.DateField(verbose_name='Fecha de Inicio')
    fechaf = models.DateField(verbose_name='Fecha Final')
    objetiv = models.CharField(max_length=64, verbose_name='Objetivos:', default='')
    meta = models.CharField(max_length=64, verbose_name='Meta:', default='')

#BASE DE DATOS DEL MODULO ACTIVIDADES
class Actividades(models.Model):
    fechai = models.DateField(verbose_name='Fecha de Inicio')
    fechaf = models.DateField(verbose_name='Fecha Final')
    objetiv = models.CharField(max_length=64, verbose_name='Objetivos:', default='')
    meta = models.CharField(max_length=64, verbose_name='Meta:', default='')

#BASE DE DATOS DE LLAMADAS
class Llamadas(models.Model):
    estado = models.CharField(max_length=64, verbose_name='Estado:', default='')
    mes = models.CharField(max_length=64, verbose_name='Mes:', default='')
    informativa = models.CharField(max_length=64, verbose_name='Informativa:', default='')
    falsa = models.CharField(max_length=64, verbose_name='Falsa:', default='')
    realesno = models.CharField(max_length=64, verbose_name='Reales no Efectivas:', default='')
    realesf = models.CharField(max_length=64, verbose_name='Reales Efectivas:', default='')
    videop = models.CharField(max_length=64, verbose_name='Video Protección:', default='')

class Infraestructura(models.Model):
    mes = models.CharField(max_length=64, verbose_name='Mes:', default='')
    estado = models.CharField(max_length=64, verbose_name='Estado:', default='')
    infraestructura = models.CharField(max_length=64, verbose_name='Infraestrutuctura:', default='')
    cantidad = models.CharField(max_length=64, verbose_name='Cantidad:', default='')
from django.db import models
from index.mixins.BaseModel import BaseModel


# Create your models here.
class CuadrantePaz(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=255)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Parroquia(models.Model):
    nombre = models.CharField(max_length=255)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    id_cuadrante_paz = models.ForeignKey(CuadrantePaz, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Incidencia(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo


class OrganismoCompetente(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Emergency(BaseModel):
    denunciante = models.CharField(max_length=255)
    telefono_denunciante = models.CharField(max_length=255, blank=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    id_parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    id_incidencia = models.ForeignKey(Incidencia, on_delete=models.CASCADE)
    direccion_incidencia = models.TextField(blank=True)
    id_organismo = models.ForeignKey(OrganismoCompetente, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True)
    # Localizacion_sede soon
    datecompleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.denunciante + " by-" + self.user.username

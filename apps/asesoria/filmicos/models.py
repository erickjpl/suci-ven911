from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

ESTATUS_CHOICES = (
    ("reg", "Registrado"),
    ("pro", "En Proceso"),
    ("nop", "No Procede"),
)


class RegistroFilmico(BaseModel):
    estatus = models.CharField(max_length=3, choices=ESTATUS_CHOICES)
    camara = models.CharField(max_length=50, blank=True, null=True)
    motivo_solicitud = models.TextField(max_length=400)
    ente_solicita = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField("Dirección", max_length=150, blank=True, null=True)
    fecha_solicitud = models.DateField(blank=True, null=True)
    fecha_culminacion = models.DateField(blank=True, null=True)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.camara

    class Meta:
        verbose_name = "registro_filmico"
        verbose_name_plural = "registro_filmicos"

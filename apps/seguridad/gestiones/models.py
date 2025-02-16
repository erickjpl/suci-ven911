from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

ESTATUS_CHOICES = (
    ("Retiro - R", "Retiro - R"),
    ("Conflictos - C", "Conflictos - C"),
    ("Conflictos ajenos - CA", "Conflictos ajenos - CA"),
)
ESTATUS_CHOICES2 = (
    ("Improvisto - R", "Improvisto - R"),
    ("Accidente familiar - R", "Accidente familiar - R"),
    ("Accidente laboral - R", "Accidente laboral - R"),
    ("Retiro por renuncia - R", "Retiro por renuncia - R"),
    ("Retiro por despido - R", "Retiro por despido - R"),
    ("Confrontamiento entre personal - CA", "Confrontamiento entre personal - CA"),
    ("Hurto o pErdida de bienes - CA", "Hurto o pérdida de bienes - CA"),
    ("Confrontamiento entre personal o natural - CA", "Confrontamiento entre personal o natural - CA"),
)

class Gestion(BaseModel):
    name = models.CharField(max_length=64, verbose_name="Nombre:", default="")
    apellido = models.CharField(max_length=64, verbose_name="Apellido:", default="")
    cedula = models.CharField(max_length=64, verbose_name="Cédula:", default="")
    tipo = models.CharField(max_length=64, choices=ESTATUS_CHOICES)
    descripcion = models.CharField(max_length=64, choices=ESTATUS_CHOICES2)
    fecha = models.DateField(verbose_name="Fecha")
    direccion = models.CharField(max_length=64, verbose_name="Dirección:", default="")
    cargo = models.CharField(max_length=64, verbose_name="Cargo:", default="")
    hora = models.CharField(max_length=64, verbose_name="Hora de Entrada:", default="")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "gestion"
        verbose_name_plural = "gestiones"
        app_label = 'seguridad'
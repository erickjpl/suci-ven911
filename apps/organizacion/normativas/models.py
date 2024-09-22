from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class Normativa(BaseModel):
    name = models.CharField(
        max_length=64, verbose_name="Nombre de Normativa:", default=""
    )
    file = models.FileField(upload_to="normativas/", verbose_name="Archivo", default="")
    user = models.CharField(max_length=64, verbose_name="Usuario", default="")
    date = models.DateField(verbose_name="Fecha", blank=True)
    progre = models.CharField(max_length=64, verbose_name="Progreso:", default="")
    estado = models.BooleanField(default=False)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "normativa"
        verbose_name_plural = "normativas"

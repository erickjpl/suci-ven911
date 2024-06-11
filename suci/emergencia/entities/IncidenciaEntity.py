from index.mixins.BaseModelMixin import BaseModel

from django.db import models


class IncidenciaEntity(models.Model):
    tipo = models.CharField(max_length=180, verbose_name="Tipo de Incidencia")

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = "eme_incidencia"
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
        ordering = ["tipo"]

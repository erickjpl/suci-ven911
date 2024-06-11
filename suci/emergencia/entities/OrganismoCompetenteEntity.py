from index.mixins.BaseModelMixin import BaseModel

from django.db import models


class OrganismoCompetenteEntity(models.Model):
    nombre = models.CharField(max_length=180, verbose_name="Nombre del organismo competente")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "eme_organismo_competente"
        verbose_name = "Organismo Competente"
        verbose_name_plural = "Organismo Competentes"
        ordering = ["nombre"]

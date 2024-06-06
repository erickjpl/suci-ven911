from django.db import models
from django.forms import model_to_dict
from paneluser.BaseModel import BaseModel


class EquipamentEntity(BaseModel):
    STATUS_CHOICES = [
        ("available", "Available"),  # Disponible
        ("loaned", "Loaned"),  # Prestado
        ("maintenance", "Maintenance"),  # Mantenimiento
    ]

    name = models.CharField(max_length=100, verbose_name="Equipo")
    description = models.TextField(verbose_name="Descripción del equipo")
    status = models.CharField(
        max_length=50, verbose_name="Estatus del equipo", choices=STATUS_CHOICES
    )

    def __str__(self):
        return self.name

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "gc_equipaments"
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ["name"]

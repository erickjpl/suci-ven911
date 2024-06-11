from emergencia.entities.IncidenciaEntity import IncidenciaEntity
from emergencia.entities.OrganismoCompetenteEntity import OrganismoCompetenteEntity
from index.entities.LocalizacionEntity import ParroquiaEntity
from index.mixins.BaseModelMixin import BaseModel

from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, TextField


class EmergencyEntity(BaseModel):
    parroquia = ForeignKey(ParroquiaEntity, on_delete=CASCADE, verbose_name="Parroquia")
    organismo = ForeignKey(OrganismoCompetenteEntity, on_delete=CASCADE, verbose_name="Organismo")
    incidencia = ForeignKey(IncidenciaEntity, on_delete=CASCADE, verbose_name="Incidencia")

    denunciante = CharField(max_length=150, verbose_name="Denunciante")
    telefono_denunciante = CharField(max_length=25, blank=True, verbose_name="Telefono del Denunciante")
    direccion_incidencia = TextField(blank=True, verbose_name="Dirección de la Incidencia")
    observaciones = TextField(blank=True, verbose_name="Observaciones")
    datecompleted = DateTimeField(null=True, blank=True, verbose_name="Fecha de finalizacion")

    def __str__(self):
        return f"Emergancia {self.incidencia}, denunciante {self.denunciante}"

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "eme_emergencia"
        verbose_name = "Emergencia"
        verbose_name_plural = "Emergencias"
        ordering = ["incidencia_id"]

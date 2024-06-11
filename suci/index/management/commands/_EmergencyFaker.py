import json
import random

from emergencia.entities.IncidenciaEntity import IncidenciaEntity
from emergencia.entities.OrganismoCompetenteEntity import OrganismoCompetenteEntity

from django.core.management.base import BaseCommand


class EmergencyFaker:
    def incidencias(fake):
        for _ in range(9):
            IncidenciaEntity.objects.create(
                tipo=fake.paragraph(nb_sentences=1),
            )
        incidencias = IncidenciaEntity.objects.count()
        print(f"Se registraron {incidencias} tipo de incidencias en la base de datos")

    def organismos_competentes(fake):
        for _ in range(12):
            OrganismoCompetenteEntity.objects.create(
                nombre=fake.paragraph(nb_sentences=1),
            )
        organismosCompetentes = OrganismoCompetenteEntity.objects.count()
        print(f"Se registraron {organismosCompetentes} organismos competentes en la base de datos")

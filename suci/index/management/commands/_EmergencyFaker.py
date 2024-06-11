import json
import random

from emergencia.entities.EmergencyEntity import EmergencyEntity
from emergencia.entities.IncidenciaEntity import IncidenciaEntity
from emergencia.entities.OrganismoCompetenteEntity import OrganismoCompetenteEntity
from index.entities.LocalizacionEntity import ParroquiaEntity

from django.core.management.base import BaseCommand
from django.utils.timezone import get_current_timezone


class EmergencyFaker:
    incidencias = 0
    organismosCompetentes = 0

    def incidencias(fake):
        for _ in range(9):
            IncidenciaEntity.objects.create(
                tipo=fake.paragraph(nb_sentences=1),
            )
        EmergencyFaker.incidencias = IncidenciaEntity.objects.count()
        print(f"Se registraron {EmergencyFaker.incidencias} tipo de incidencias en la base de datos")

    def organismos_competentes(fake):
        for _ in range(12):
            OrganismoCompetenteEntity.objects.create(
                nombre=fake.paragraph(nb_sentences=1),
            )
        EmergencyFaker.organismosCompetentes = OrganismoCompetenteEntity.objects.count()
        print(f"Se registraron {EmergencyFaker.organismosCompetentes} organismos competentes en la base de datos")

    def emergencias(fake, parroquias, guest):
        parroquias = ParroquiaEntity.objects.count() if parroquias == 0 else parroquias
        for _ in range(30):
            pk_parroquia = random.randint(1, parroquias)
            pk_organismo_competente = random.randint(1, EmergencyFaker.organismosCompetentes)
            pk_incidencia = random.randint(1, EmergencyFaker.incidencias)

            parroquia = ParroquiaEntity.objects.get(pk=pk_parroquia)
            organismo_competente = OrganismoCompetenteEntity.objects.get(pk=pk_organismo_competente)
            incidencia = IncidenciaEntity.objects.get(pk=pk_incidencia)

            EmergencyEntity.objects.create(
                parroquia=parroquia,
                organismo=organismo_competente,
                incidencia=incidencia,
                denunciante=fake.name(),
                telefono_denunciante=fake.phone_number(),
                direccion_incidencia=fake.address(),
                observaciones=fake.paragraph(nb_sentences=1),
                datecompleted=fake.date_time(get_current_timezone()) if fake.boolean() else None,
                created_by=guest,
                updated_by=guest,
            )
        emergencias = EmergencyEntity.objects.count()
        print(f"Se registraron {emergencias} emergencias en la base de datos")

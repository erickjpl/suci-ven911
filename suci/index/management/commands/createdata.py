import random

import faker.providers
from faker import Faker
from index.management.commands._EmergencyFaker import EmergencyFaker
from index.management.commands._GestionComunicacionalFaker import GestionComunicacionalFaker
from index.management.commands._LocalizacionFaker import LocalizacionFaker
from paneluser.models import UserEntity

from django.core.management.base import BaseCommand

STATUS_CHOICES = [
    "available",
    "loaned",
    "maintenance",
]

ACTIVITY_TYPE_CHOICES = [
    "workshop",
    "conference",
    "campaign",
]

PLATFORM_CHOICES = [
    "Facebook",
    "Instagram",
    "Twitter",
]


class Provider(faker.providers.BaseProvider):
    def equipments_status(self):
        return self.random_element(STATUS_CHOICES)

    def social_activity_type(self):
        return self.random_element(ACTIVITY_TYPE_CHOICES)

    def social_media_account_platform(self):
        return self.random_element(PLATFORM_CHOICES)


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker("es_ES")
        fake.add_provider(Provider)

        admin = UserEntity.objects.filter(dni=100).first()
        if admin is None:
            admin = UserEntity.objects.create(
                dni=100,
                first_name="Admin",
                last_name="Admin",
                username="admin",
                email="admin@suci.com",
                password="pbkdf2_sha256$720000$Kz9kinsPg3DmSui1Piw5vy$P9/hiiwNCkYmFuXdDLrP8ZVXctTk7eU0odL2FIMmeEU=",
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
            print(
                f"Usuario {admin.username} con cédula de identidad {admin.dni} creado como superusuario, su contraseña: admin"
            )
        guest = UserEntity.objects.filter(dni=200).first()
        if guest is None:
            guest = UserEntity.objects.create(
                dni=200,
                first_name="Guest",
                last_name="Guest",
                username="guest",
                email="guest@suci.com",
                password="pbkdf2_sha256$720000$4ojJVNjkvfY3KcZsqfYIgu$ZWb6ndDEB96vo0mTbmIEIXJaxT7wbCVdWisnm0irPFA=",
                is_staff=True,
                is_active=True,
                is_superuser=False,
            )
            print(
                f"Usuario {guest.username} con cédula de identidad {guest.dni} creado como usuario, su contraseña: guest"
            )

        GestionComunicacionalFaker.Equipment(fake, admin, guest)
        GestionComunicacionalFaker.SocialActivity(fake, admin, guest)
        GestionComunicacionalFaker.SocialMediaAccount(fake, admin, guest)

        LocalizacionFaker.cupaz(fake)
        LocalizacionFaker.estados()
        LocalizacionFaker.ciudades()
        LocalizacionFaker.municipios()
        LocalizacionFaker.parroquias()

        EmergencyFaker.incidencias(fake)
        EmergencyFaker.organismos_competentes(fake)

import random

import faker.providers
from faker import Faker
from index.management.commands._EmergencyFaker import EmergencyFaker
from index.management.commands._GestionComunicacionalFaker import GestionComunicacionalFaker
from index.management.commands._LocalizacionFaker import LocalizacionFaker
from index.management.commands._UserAndPermissionFaker import UserAndPermissionFaker
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
    parroquias = 0

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
        other = UserEntity.objects.filter(dni=300).first()
        if other is None:
            other = UserEntity.objects.create(
                dni=300,
                first_name="Other",
                last_name="Other",
                username="other",
                email="other@suci.com",
                password="pbkdf2_sha256$720000$Qr3Og7wGXM7qADiK7Vlx7V$Q8D6HF/H5CzO3W0ub+CTnwMjdnTzWdqJjxD78YEcTf0=",
                is_staff=False,
                is_active=True,
                is_superuser=False,
            )
            print(
                f"Usuario {other.username} con cédula de identidad {other.dni} creado como usuario, su contraseña: other"
            )

        UserAndPermissionFaker.create_permissions()
        UserAndPermissionFaker.user_permissions(guest)
        # UserAndPermissionFaker.create_group()
        # UserAndPermissionFaker.group_permissions()
        # UserAndPermissionFaker.user_groups()

        GestionComunicacionalFaker.equipment(fake, admin, guest)
        GestionComunicacionalFaker.social_activity(fake, admin, guest)
        GestionComunicacionalFaker.social_media_account(fake, admin, guest)

        LocalizacionFaker.cupaz(fake)
        LocalizacionFaker.estados()
        LocalizacionFaker.ciudades()
        LocalizacionFaker.municipios()
        self.parroquias = LocalizacionFaker.parroquias()

        EmergencyFaker.incidencias(fake)
        EmergencyFaker.organismos_competentes(fake)
        EmergencyFaker.emergencias(fake, self.parroquias, guest)

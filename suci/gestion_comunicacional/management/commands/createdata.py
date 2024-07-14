import random

import faker.providers
from faker import Faker
from gestion_comunicacional.management.commands._BienesFaker import BienesFaker
from gestion_comunicacional.management.commands._GestionComunicacionalFaker import GestionComunicacionalFaker
from gestion_comunicacional.management.commands._UserAndPermissionFaker import UserAndPermissionFaker
from paneluser.models import Usuarios

from django.core.management.base import BaseCommand

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

BIEN_NACIONAL = [
    "Computador de Escritorio",
    "Laptop",
    "Servidor",
    "Impresora",
    "Camara",
    "Televisor",
    "Amplificador",
]


class Provider(faker.providers.BaseProvider):
    def social_activity_type(self):
        return self.random_element(ACTIVITY_TYPE_CHOICES)

    def social_media_account_platform(self):
        return self.random_element(PLATFORM_CHOICES)

    def bien_nacional(self):
        return self.random_element(BIEN_NACIONAL)


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker("es_ES")
        fake.add_provider(Provider)

        admin = Usuarios.objects.filter(username=100).first()
        if admin is None:
            admin = Usuarios.objects.create(
                username=100,
                first_name="Admin",
                last_name="Admin",
                email="admin@suci.com",
                password="pbkdf2_sha256$720000$Kz9kinsPg3DmSui1Piw5vy$P9/hiiwNCkYmFuXdDLrP8ZVXctTk7eU0odL2FIMmeEU=",
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
            print(
                f"Usuario {admin.username} con cédula de identidad {admin.username} creado como superusuario, su contraseña: admin"
            )
        guest = Usuarios.objects.filter(username=200).first()
        if guest is None:
            guest = Usuarios.objects.create(
                username=200,
                first_name="Guest",
                last_name="Guest",
                email="guest@suci.com",
                password="pbkdf2_sha256$720000$4ojJVNjkvfY3KcZsqfYIgu$ZWb6ndDEB96vo0mTbmIEIXJaxT7wbCVdWisnm0irPFA=",
                is_staff=True,
                is_active=True,
                is_superuser=False,
            )
            print(
                f"Usuario {guest.username} con cédula de identidad {guest.username} creado como usuario, su contraseña: guest"
            )
        other = Usuarios.objects.filter(username=300).first()
        if other is None:
            other = Usuarios.objects.create(
                username=300,
                first_name="Other",
                last_name="Other",
                email="other@suci.com",
                password="pbkdf2_sha256$720000$Qr3Og7wGXM7qADiK7Vlx7V$Q8D6HF/H5CzO3W0ub+CTnwMjdnTzWdqJjxD78YEcTf0=",
                is_staff=False,
                is_active=True,
                is_superuser=False,
            )
            print(
                f"Usuario {other.username} con cédula de identidad {other.username} creado como usuario, su contraseña: other"
            )

        UserAndPermissionFaker.create_permissions()
        UserAndPermissionFaker.user_permissions(guest)

        GestionComunicacionalFaker.social_activity(fake, admin, guest)
        GestionComunicacionalFaker.social_media_account(fake, admin, guest)
        
        BienesFaker.add_departamento()
        BienesFaker.add_sedes()
        BienesFaker.add_bienes(fake)
        
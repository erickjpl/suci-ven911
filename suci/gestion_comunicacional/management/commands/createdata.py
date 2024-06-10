import random

import faker.providers
from faker import Faker
from gestion_comunicacional.equipments.entities.EquipmentEntity import EquipmentEntity
from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity
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
        guest = UserEntity.objects.create(
            dni=200,
            first_name="Guest",
            last_name="Guest",
            username="guest",
            email="guest@suci.com",
            password="pbkdf2_sha256$720000$4ojJVNjkvfY3KcZsqfYIgu$ZWb6ndDEB96vo0mTbmIEIXJaxT7wbCVdWisnm0irPFA=",
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        print(f"Usuario {guest.username} con cédula de identidad {guest.dni} creado como usuario, su contraseña: guest")

        for _ in range(30):
            equipments = EquipmentEntity.objects.create(
                name=fake.paragraph(nb_sentences=1),
                description=fake.paragraph(nb_sentences=3),
                status=fake.equipments_status(),
                created_by=admin,
                updated_by=guest,
            )
        equipments_count = EquipmentEntity.objects.count()
        print(f"Hay {equipments_count} equipos en la base de datos")

        for _ in range(60):
            social_activities = SocialActivityEntity.objects.create(
                activity_type=fake.social_activity_type(),
                date=fake.date(),
                location=fake.address(),
                description=fake.paragraph(nb_sentences=3),
                reason=fake.text(max_nb_chars=80),
                beneficiaries=random.randint(18, 1990),
                created_by=admin,
                updated_by=guest,
            )
        social_activities_count = SocialActivityEntity.objects.count()
        print(f"Hay {social_activities_count} actividades sociales en la base de datos")

        for _ in range(15):
            social_activities = SocialMediaAccountEntity.objects.create(
                platform=fake.social_media_account_platform(),
                username_sm=fake.unique.user_name(),
                url=fake.unique.url(),
                followers=random.randint(1811, 19900),
                responsible=fake.name(),
                publications=random.randint(1811, 1990),
                created_by=admin,
                updated_by=guest,
            )
        social_media_account_count = SocialMediaAccountEntity.objects.count()
        print(f"Hay {social_media_account_count} cuentas de redes sociales en la base de datos")

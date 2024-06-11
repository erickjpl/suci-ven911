import random

from gestion_comunicacional.equipments.entities.EquipmentEntity import EquipmentEntity
from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity


class GestionComunicacionalFaker:
    def SocialMediaAccount(fake, admin, guest):
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

    def Equipment(fake, admin, guest):
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

    def SocialActivity(fake, admin, guest):
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

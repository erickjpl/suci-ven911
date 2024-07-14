import random

from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity

from django.db.models import Q


class GestionComunicacionalFaker:
    def social_media_account(fake, admin, guest):
        for _ in range(15):
            user_name = fake.unique.user_name()
            url = fake.unique.url()
            try:
                obj = SocialMediaAccountEntity.objects.get(Q(username_sm=user_name) | Q(url=url))
            except SocialMediaAccountEntity.DoesNotExist:
                social_activities = SocialMediaAccountEntity.objects.update_or_create(
                    platform=fake.social_media_account_platform(),
                    username_sm=fake.user_name,
                    url=url,
                    followers=random.randint(1811, 19900),
                    responsible=fake.name(),
                    publications=random.randint(1811, 1990),
                    created_by=admin,
                    updated_by=guest,
                )

        social_media_account_count = SocialMediaAccountEntity.objects.count()
        print(f"Hay {social_media_account_count} cuentas de redes sociales en la base de datos")

    def social_activity(fake, admin, guest):
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

import factory
from faker import Faker

from .models import EquipamentEntity, SocialActivityEntity, SocialMediaAccountEntity

fake = Faker("es_ES")


class EquipamentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EquipamentEntity

    name = factory.Faker("sentence", min_chars=5, max_chars=50)
    description = factory.Faker("paragraph", sentences=3)
    status = factory.Faker("random_element", elements=EquipamentEntity.STATUS_CHOICES)


class SocialActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SocialActivityEntity

    activity_type = factory.Faker("random_element", elements=SocialActivityEntity.ACTIVITY_TYPE_CHOICES)
    date = factory.Faker("date")
    location = factory.Faker("address")
    description = factory.Faker("paragraph", sentences=5)
    reason = factory.Faker("text", max_nb_chars=200)
    beneficiaries = factory.Faker("pyint", min_value=10, max_value=200)


class SocialMediaAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SocialMediaAccountEntity

    platform = factory.Faker("random_element", elements=SocialMediaAccountEntity.PLATFORM_CHOICES)
    username_sm = factory.Faker("user_name")
    url = factory.Faker("url")
    followers = factory.Faker("pyint", min_value=100, max_value=10000)
    responsible = factory.Faker("name")
    publications = factory.Faker("pyint", min_value=10, max_value=50)

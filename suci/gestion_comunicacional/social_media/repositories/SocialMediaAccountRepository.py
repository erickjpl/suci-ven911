from gestion_comunicacional.mixins.RepositoryMixin import Repository
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity

from django.db.models import Sum


class SocialMediaAccountRepository(Repository):
    def __init__(self):
        self.entity = SocialMediaAccountEntity

    def getInfo(self):
        return self.entity.objects.values("platform").annotate(total_publications=Sum("publications"), total_followers=Sum("followers"))

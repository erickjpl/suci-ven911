from gestion_comunicacional.mixins.CrudMixin import CrudService
from gestion_comunicacional.social_media.repositories.SocialMediaAccountRepository import SocialMediaAccountRepository

from django.db.models import Q


class SocialMediaAccountService(CrudService):
    def __init__(self):
        self.repository = SocialMediaAccountRepository()

    def getAll(self, draw, start, length, search=None, select=("")):
        query = None
        if search:
            query = Q()
            for column in ["id", "platform", "username_sm", "responsible"]:
                query |= Q(**{f"{column}__icontains": search})

        return super().getAll(draw, start, length, query, select)

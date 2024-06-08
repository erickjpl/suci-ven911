from gestion_comunicacional.social_activity.repositories.SocialActivityRepository import SocialActivityRepository
from index.mixins.CrudMixin import CrudService


class SocialActivityService(CrudService):
    def __init__(self):
        self.repository = SocialActivityRepository()

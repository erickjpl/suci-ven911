from gestion_comunicacional.mixins.RepositoryMixin import Repository
from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity


class SocialActivityRepository(Repository):
    def __init__(self):
        self.entity = SocialActivityEntity

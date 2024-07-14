from entities.SocialMediaPostEntity import SocialMediaPostEntity
from gestion_comunicacional.mixins.RepositoryMixin import Repository


class SocialMediaPostRepository(Repository):
    def __init__(self):
        self.entity = SocialMediaPostEntity

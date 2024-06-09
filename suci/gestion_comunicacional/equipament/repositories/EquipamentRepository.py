from gestion_comunicacional.equipament.entities.EquipamentEntity import EquipamentEntity
from index.mixins.RepositoryMixin import Repository


class EquipamentRepository(Repository):
    def __init__(self):
        self.entity = EquipamentEntity

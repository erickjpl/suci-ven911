from gestion_comunicacional.equipament.repositories.EquipamentRepository import EquipamentRepository
from index.mixins.CrudMixin import CrudService


class EquipamentService(CrudService):
    def __init__(self):
        self.repository = EquipamentRepository()

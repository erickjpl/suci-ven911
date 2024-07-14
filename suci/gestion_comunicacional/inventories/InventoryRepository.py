from gestion_comunicacional.mixins.RepositoryMixin import Repository
from rrhh.models import Bienes, Departamento


class InventoryRepository(Repository):
    def __init__(self):
        self.entity = Bienes

    def getInfo(self):
        departamento = Departamento.objects.get(departamento='Gestion Comunicacional')

        return self.entity.objects.filter(departamento=departamento).values(*("estatus", "sede__sede", "nombre", "cantidad"))[:5]

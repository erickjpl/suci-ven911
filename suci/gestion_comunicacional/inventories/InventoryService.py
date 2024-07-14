from gestion_comunicacional.inventories.InventoryRepository import InventoryRepository
from gestion_comunicacional.mixins.CrudMixin import CrudService

from django.db.models import Q


class InventoryService(CrudService):
    def __init__(self):
        self.repository = InventoryRepository()

    def getAll(self, draw, start, length, search=None, select=("")):
        query = None
        if search:
            query = Q()
            for column in ["id", "platform", "username_sm", "responsible"]:
                query |= Q(**{f"{column}__icontains": search})

        return super().getAll(draw, start, length, query, select)

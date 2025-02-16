from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import EntradaRepository


class EntradaService(CrudService):
    def __init__(self):
        self.repository = EntradaRepository()

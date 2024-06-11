from emergencia.EmergencyRepository import EmergencyRepository
from index.mixins.CrudMixin import CrudService


class EmergencyService(CrudService):
    def __init__(self):
        self.repository = EmergencyRepository()

from emergencia.entities.EmergencyEntity import EmergencyEntity
from index.mixins.RepositoryMixin import Repository


class EmergencyRepository(Repository):
    def __init__(self):
        self.entity = EmergencyEntity

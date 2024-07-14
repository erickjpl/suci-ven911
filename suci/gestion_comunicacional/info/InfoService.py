from gestion_comunicacional.inventories.InventoryRepository import InventoryRepository
from gestion_comunicacional.mixins.CrudMixin import CrudService
from gestion_comunicacional.social_activity.repositories.SocialActivityRepository import SocialActivityRepository
from gestion_comunicacional.social_media.repositories.SocialMediaAccountRepository import SocialMediaAccountRepository


class InfoService(CrudService):
    def __init__(self):
        self.socialActivityRepository = SocialActivityRepository()
        self.socialMediarepository = SocialMediaAccountRepository()
        self.inventoryRepository = InventoryRepository()

    def info(self):
      return {
        "activity": {
          "activities": self.socialActivityRepository.getAll().count(),
          "beneficiaries": self.socialActivityRepository.getAll().count(),
        },
        "account": list(self.socialMediarepository.getInfo()),
        "inventroies": list(self.inventoryRepository.getInfo())
      }

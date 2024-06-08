from django.core.exceptions import ValidationError

from gestion_comunicacional.equipament.repositories.EquipamentRepository import EquipamentRepository
from index.mixins.RequestDataMixin import RequestDataMixin


class EquipamentService(RequestDataMixin):
    def __init__(self):
        self.repository = EquipamentRepository()

    def getAll(self, page, search=None):
        if search is None:
            entities = self.repository.getAll()
        else:
            entities = self.repository.getAllFilter(search)

        # paginator = Paginator(entities, 15)

        # return PaginatorUtil.paginate(paginator, page)
        return entities

    def creator(self, form, request):
        data = self.prepare_data(request)
        if form.is_valid():
            form.clean()
            return self.repository.create(data)
        raise ValidationError(form.errors.as_json())

    def reader(self, id):
        return self.repository.getById(id)

    def updater(self, put, id):
        return self.repository.updateWithForm(id, put)

    def destroyer(self, id):
        return self.repository.delete(id)

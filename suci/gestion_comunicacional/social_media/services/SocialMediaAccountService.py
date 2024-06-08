from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from gestion_comunicacional.social_media.repositories.SocialMediaAccountRepository import (
    SocialMediaAccountRepository,
)
from gestion_comunicacional.utils.PaginatorUtil import PaginatorUtil
from index.mixins.RequestDataMixin import RequestDataMixin


class SocialMediaAccountService(RequestDataMixin):
    def __init__(self):
        self.repository = SocialMediaAccountRepository()

    def getAll(self, page, search=None):
        if search is None:
            entities = self.repository.getAll()
        else:
            entities = self.repository.getAllFilter(search)

        entities = self.repository.getAll()
        paginator = Paginator(entities, 15)

        return PaginatorUtil.paginate(paginator, page)

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

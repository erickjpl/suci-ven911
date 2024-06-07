from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from gestion_comunicacional.social_media.forms.SocialMediaAccountForm import (
    SocialMediaAccountForm,
)
from gestion_comunicacional.social_media.repositories.SocialMediaAccountRepository import (
    SocialMediaAccountRepository,
)
from gestion_comunicacional.utils.PaginatorUtil import PaginatorUtil


class SocialMediaAccountService:
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

    def creator(self, request):
        data = request.POST.copy()
        data["created_by"] = request.user
        data["updated_by"] = request.user

        form = SocialMediaAccountForm(data)

        if form.is_valid():
            return self.repository.create(data)

        for field in form.errors:
            form[field].field.widget.attrs["class"] += " is-invalid"

        raise ValidationError(form)

    def reader(self, id):
        return self.repository.getById(id)

    def updater(self, put, id):
        return self.repository.updateWithForm(id, put)

    def destroyer(self, id):
        return self.repository.delete(id)

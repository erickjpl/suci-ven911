from index.mixins.ServiceUtilMixin import ServiceUtilMixin

from django.core.exceptions import ValidationError


class CrudService(ServiceUtilMixin):
    def getAll(self, page, search=None):
        if search is None:
            entities = self.repository.getAll()
        else:
            entities = self.repository.getAllFilter(search)

        data = []
        for item in self.paginate(entities, page):
            data.append(item.toJSON())

        return data

    def creator(self, form, request):
        data = self.prepare_data(request)
        if form.is_valid():
            form.clean()
            return self.repository.create(data)
        raise ValidationError(form.errors.as_json())

    def reader(self, id):
        try:
            return self.repository.getById(id)
        except Usuario.DoesNotExist:
            raise Http404("La cuenta de la red social no se ha encontrada")

    def updater(self, form, id, request):
        return self.repository.updateWithForm(id, put)

    def destroyer(self, id):
        return self.repository.delete(id)

from gestion_comunicacional.mixins.ServiceUtilMixin import ServiceUtilMixin

from django.core.exceptions import ValidationError
from django.http import Http404


class CrudService(ServiceUtilMixin):
    def getAll(self, draw, start, length, search=None, select=("")):
        if search is None:
            entities = self.repository.getAll(select)
        else:
            entities = self.repository.getFilter(search, select)

        return self.response(entities, start, length, draw)

    def creator(self, form, request):
        data = self.prepare_data(request)
        if form.is_valid():
            form.clean()
            return self.repository.create(data)
        raise ValidationError(form.errors.as_json())

    def reader(self, id, select=("")):
        try:
            return self.repository.getById(id, select)
        except Exception as e:
            raise Http404("No se ha encontrado el recurso.")

    def updater(self, entity, payload):
        if payload.is_valid():
            payload.clean()
            return self.repository.update(entity, payload)
        raise ValidationError(payload.errors.as_json())

    def destroyer(self, payload):
        return self.repository.delete(payload)

    class Meta:
        abstract = True

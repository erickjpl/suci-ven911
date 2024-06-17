from index.mixins.ServiceUtilMixin import ServiceUtilMixin

from django.core.exceptions import ValidationError


class CrudService(ServiceUtilMixin):
    def getAll(self, draw, start, length, search=None, select=("")):
        response = {}

        if search is None:
            entities = self.repository.getAll(select)
        else:
            entities = self.repository.getFilter(search, select)

        data = []
        for item in self.paginate(entities, start, length, draw):
            data.append(item)

        records_total = entities.count()

        response["draw"] = draw
        response["entities"] = data
        response["recordsTotal"] = records_total
        response["recordsFiltered"] = records_total

        return response

    def creator(self, form, request):
        data = self.prepare_data(request)
        if form.is_valid():
            form.clean()
            return self.repository.create(data)
        raise ValidationError(form.errors.as_json())

    def reader(self, id, select=("")):
        try:
            return self.repository.getById(id, select)
        except Usuario.DoesNotExist:
            raise Http404("La cuenta de la red social no se ha encontrada")

    def updater(self, entity, payload):
        if payload.is_valid():
            payload.clean()
            return self.repository.update(entity, payload)
        raise ValidationError(payload.errors.as_json())

    def destroyer(self, payload):
        return self.repository.delete(payload)

    class Meta:
        abstract = True

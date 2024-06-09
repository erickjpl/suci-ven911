from index.mixins.ServiceUtilMixin import ServiceUtilMixin

from django.core.exceptions import ValidationError
from django.http import Http404


class Repository:
    def getAll(self):
        return self.entity.objects.all()

    def getFilter(self, search):
        return self.entity.objects.filter(username=search)

    def getById(self, id):
        try:
            return self.entity.objects.get(pk=id)
        except self.entity.DoesNotExist:
            raise Http404

    def create(self, data):
        data = {k: v for k, v in data.items() if k != "csrfmiddlewaretoken"}
        entity = self.entity(**data)
        entity.save()
        return entity

    def update(self, entity, payload):
        for field in payload.fields:
            if hasattr(entity, field):
                setattr(entity, field, payload.cleaned_data[field])
        entity.save()
        return entity

    def delete(self, id):
        return self.getById(id).delete()

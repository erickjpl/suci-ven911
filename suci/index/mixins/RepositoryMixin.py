from index.mixins.ServiceUtilMixin import ServiceUtilMixin

from django.core.exceptions import ValidationError


class Repository:
    def getAll(self):
        return self.entity.objects.all()

    def getFilter(self, search):
        return self.entity.objects.filter(username=search)

    def getById(self, id):
        return self.entity.objects.get(id=id)

    def create(self, data):
        data = {k: v for k, v in data.items() if k != "csrfmiddlewaretoken"}

        entity = self.entity(**data)
        entity.save()
        return entity

    def update(self, id, data):
        entity = self.getById(id)
        for field, value in data.items():
            setattr(entity, field, value)
        entity.save()
        return entity

    def delete(self, id):
        return self.getById(id).delete()

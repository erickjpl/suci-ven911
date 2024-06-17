from index.mixins.BaseModelMixin import BaseModel

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class ServiceUtilMixin:
    def prepare_data(self, request):
        data = request.POST.copy()
        user = request.user
        if data.get("id") is None:
            data["created_by"] = user
        data["updated_by"] = user
        return data

    def paginate(self, data, start, length, draw):
        entities = data[start : start + length]
        paginator = Paginator(entities, length)

        try:
            items = paginator.page(draw).object_list
        except PageNotAnInteger:
            items = paginator.page(draw).object_list
        except EmptyPage:
            items = paginator.page(paginator.num_pages).object_list
        return items

    class Meta:
        abstract = True

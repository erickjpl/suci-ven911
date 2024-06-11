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

    def paginate(self, entities, page):
        paginator = Paginator(entities, 15)

        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        return items

    class Meta:
        abstract = True

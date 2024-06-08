from django.core.paginator import Paginator


class ServiceUtilMixin:
    def prepare_data(self, request):
        data = request.POST.copy()
        data["created_by"] = request.user
        data["updated_by"] = request.user
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

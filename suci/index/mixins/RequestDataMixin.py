class RequestDataMixin:
    def prepare_data(self, request):
        data = request.POST.copy()
        data["created_by"] = request.user
        data["updated_by"] = request.user
        return data

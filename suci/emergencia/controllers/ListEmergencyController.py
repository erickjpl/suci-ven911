from emergencia.EmergencyService import EmergencyService
from index.mixins.ControllerMixin import ListController
from templates.sneat import TemplateLayout

from django.urls import reverse_lazy


class ListEmergency(ListController):
    template_name = "emergencia/listing.html"

    def __init__(self):
        self.service = EmergencyService()

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "eme_title_page"
        context["indexUrl"] = reverse_lazy("eme:list-emergency")
        context["module"] = "eme_module_name"
        context["submodule"] = "eme_emergencia_module_name"
        context["createBtn"] = "eme_title_btn_add"
        context["createUrl"] = reverse_lazy("eme:create-emergency")
        context["listUrl"] = reverse_lazy("eme:list-emergency")
        context["updateUrl"] = reverse_lazy("eme:update-emergency", args=[0])
        context["deleteUrl"] = reverse_lazy("eme:delete-emergency", args=[0])
        context["columns"] = "id|denunciante|telefono_denunciante|datecompleted"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        page = self.request.GET.get("page") or 1
        search = self.request.GET.get("search") or {"datecompleted__isnull": True}

        return self.service.getAll(page, search, ("id", "denunciante", "telefono_denunciante", "datecompleted"))

import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import EntradaService
from ..models import Entrada

class EntradaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Entradas"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("entradas:create")
        context["listApiUrl"] = reverse_lazy("api_entradas:list")
        context["updateUrl"] = reverse_lazy("entradas:update", args=[0])
        context["deleteUrl"] = reverse_lazy("entradas:delete", args=[0])
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "name",
                "name": "name",
                "title": "Nombre",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "apellido",
                "name": "apellido",
                "title": "Apellido",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "cedula",
                "name": "cedula",
                "title": "Cédula",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "telefono",
                "name": "telefono",
                "title": "Teléfono",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "fecha",
                "name": "fecha",
                "title": "Fecha del incidente",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "direccion",
                "name": "direccion",
                "title": "Dirección",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "cargo",
                "name": "cargo",
                "title": "Cargo",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "hora",
                "name": "hora",
                "title": "Hora",
                "orderable": "true",
                "searchable": "true",
            },
        ]

class EntradaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = EntradaService()

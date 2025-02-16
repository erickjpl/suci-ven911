import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import VehiculoService
from ..models import Vehiculo

class VehiculoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Vehículo"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("vehiculo:create")
        context["listApiUrl"] = reverse_lazy("api_vehiculo:list")
        context["updateUrl"] = reverse_lazy("vehiculo:update", args=[0])
        context["deleteUrl"] = reverse_lazy("vehiculo:delete", args=[0])
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
            return [
                {
                    "data": "nombre",
                    "name": "nombre",
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
                    "data": "modelo",
                    "name": "modelo",
                    "title": "Modelo del Vehículo",
                    "orderable": "true",
                    "searchable": "true",
                },
                {
                    "data": "motivo",
                    "name": "motivo",
                    "title": "Motivo",
                    "orderable": "true",
                    "searchable": "true",
                },
                {
                    "data": "capagasolina",
                    "name": "capagasolina",
                    "title": "Capacidad de gasolina",
                    "orderable": "true",
                    "searchable": "true",
                },
                {
                    "data": "cantigasolina",
                    "name": "cantigasolina",
                    "title": "Cantidad de gasolina",
                    "orderable": "true",
                    "searchable": "true",
                },
                {
                    "data": "placa",
                    "name": "placa",
                    "title": "Placa",
                    "orderable": "true",
                    "searchable": "true",
                },
                {
                    "data": "fecha",
                    "name": "fecha",
                    "title": "Fecha",
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

class VehiculoListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = VehiculoService()

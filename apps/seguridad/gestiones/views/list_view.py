import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from seguridad.gestiones.services import GestionService


class GestionListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Gestions"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("gestiones:create")
        context["listApiUrl"] = reverse_lazy("api_gestiones:list")
        context["updateUrl"] = reverse_lazy("gestiones:update", args=[0])
        context["deleteUrl"] = reverse_lazy("gestiones:delete", args=[0])
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "ID",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "name",
                "name": "name",
                "title": "Nombre",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "apellido",
                "name": "apellido",
                "title": "Apellido",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cedula",
                "name": "cedula",
                "title": "Cédula",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "direccion",
                "name": "direccion",
                "title": "Dirección",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "tipo",
                "name": "tipo",
                "title": "Tipo de Incidente",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "descripcion",
                "name": "descripcion",
                "title": "Descripción",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fecha",
                "name": "fecha",
                "title": "Fecha",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "hora",
                "name": "hora",
                "title": "Hora",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cargo",
                "name": "cargo",
                "title": "Cargo",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class GestionListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = GestionService()

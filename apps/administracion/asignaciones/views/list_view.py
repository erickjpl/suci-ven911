import json

from administracion.asignaciones.services import AsignacionService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout


class AsignacionListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administracion"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Administracion"
        context["submodule"] = "Asignacion"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("asignaciones:create")
        context["listApiUrl"] = reverse_lazy("asignaciones:list")
        context["updateUrl"] = reverse_lazy("asignaciones:update", args=[0])
        context["deleteUrl"] = reverse_lazy("asignaciones:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("asignaciones:export_excel")
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "#",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "articulo",
                "name": "articulo",
                "title": "Artículo",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "sede",
                "name": "sede",
                "title": "Sede",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "departamento",
                "name": "departamento",
                "title": "Departamento",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cantidad",
                "name": "cantidad",
                "title": "Cantidad",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "descripcion",
                "name": "descripcion",
                "title": "Descripción",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "observaciones",
                "name": "observaciones",
                "title": "Observaciones",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "creadopor",
                "name": "creadopor",
                "title": "Creado por",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class AsignacionListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = AsignacionService()

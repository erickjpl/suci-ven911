from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from rrhh.tipos_sueldos.forms import TipoSueldoForm
from rrhh.tipos_sueldos.models import TipoSueldo
from rrhh.tipos_sueldos.services import TipoSueldoService


class TipoSueldoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Tipos de Sueldos"
        context["titleForm"] = "Eliminar tipo de empleado"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("tipos_sueldos:list")
        context["urlDelete"] = reverse_lazy(
            "api_tipos_sueldos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return TipoSueldo.objects.filter(pk=id)


class TipoSueldoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = TipoSueldoForm

    def __init__(self):
        self.service = TipoSueldoService()

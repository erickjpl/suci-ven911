import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout

class SeguridadView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Dashboard Protección y Seguridad Integral"
        context["submoduleList"] = (
            ("Entrada", reverse_lazy("entradas:list")),
            ("Salida", reverse_lazy("salida:list")),
            ("Gestión de Incidentes", reverse_lazy("gestion:list")),
            ("Vehículos", reverse_lazy("vehiculo:list")),
        )
        return TemplateLayout.init(self, context)

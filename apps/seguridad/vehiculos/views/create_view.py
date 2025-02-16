from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout
from ..forms import VehiculoForm
from ..services import VehiculoService

class VehiculoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = VehiculoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Protección y Seguridad Integral"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Protección y Seguridad Integral"
        context["submodule"] = "Vehículo"
        context["titleForm"] = "Añadir una vehiculo nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("vehiculo:list")
        context["urlForm"] = reverse_lazy("api_vehiculo:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

class VehiculoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = VehiculoForm

    def __init__(self):
        self.service = VehiculoService()

from emergencia.EmergencyForm import EmergencyForm
from emergencia.EmergencyService import EmergencyService
from index.mixins.ControllerMixin import UpdateController
from templates.sneat import TemplateLayout

from django.urls import reverse_lazy


class UpdateEmergency(UpdateController):
    form_class = EmergencyForm
    template_name = "emergencia/update.html"
    redirect_not_found = reverse_lazy("eme:list-emergency")

    def __init__(self):
        self.service = EmergencyService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "eme_title_page"
        context["indexUrl"] = reverse_lazy("eme:list-emergency")
        context["module"] = "eme_module_name"
        context["submodule"] = "eme_emergencia_module_name"
        context["titleForm"] = "eme_emergencia_title_form"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("eme:list-emergency")
        context["urlForm"] = reverse_lazy("eme:update-emergency", args=[self.kwargs.get("pk")])
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

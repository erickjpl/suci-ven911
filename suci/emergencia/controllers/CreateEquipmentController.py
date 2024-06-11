from emergencia.EmergencyForm import EmergencyForm
from emergencia.EmergencyService import EmergencyService
from index.mixins.ControllerMixin import CreateController
from templates.sneat import TemplateLayout

from django.urls import reverse_lazy


class CreateEmergency(CreateController):
    template_name = "emergencia/create.html"
    form_class = EmergencyForm

    def __init__(self):
        self.service = EmergencyService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "eme_title_page"
        context["indexUrl"] = reverse_lazy("eme:list-emergency")
        context["module"] = "eme_module_name"
        context["submodule"] = "eme_emergencia_module_name"
        context["titleForm"] = "eme_title_form"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("eme:list-emergency")
        context["urlForm"] = reverse_lazy("eme:create-emergency")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

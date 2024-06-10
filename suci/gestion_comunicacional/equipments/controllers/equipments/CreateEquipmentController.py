import json

from gestion_comunicacional.equipments.forms.EquipmentForm import EquipmentForm
from gestion_comunicacional.equipments.services.EquipmentService import EquipmentService
from templates.sneat import TemplateLayout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView


class CreateEquipment(LoginRequiredMixin, CreateView):
    template_name = "gc/equipments/equipments/create.html"
    form_class = EquipmentForm

    def __init__(self):
        self.service = EquipmentService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_eq_equipments_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_eq_module_name"
        context["titleForm"] = "gc_eq_equipments_title_form"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("gc:eq:listing-equipments")
        context["urlForm"] = reverse_lazy("gc:eq:create-equipments")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

    def post(self, request, *arg, **kwargs):
        if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
            try:
                self.service.creator(self.get_form(), request)
                return JsonResponse({"message": "Se ha registro con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message.replace("'", '"'))})

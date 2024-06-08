import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView

from gestion_comunicacional.equipament.forms.EquipamentForm import EquipamentForm
from gestion_comunicacional.equipament.services.EquipamentService import EquipamentService
from templates.sneat import TemplateLayout


class CreateEquipament(LoginRequiredMixin, CreateView):
    template_name = "gc/equipaments/equipaments/create.html"
    form_class = EquipamentForm

    def __init__(self):
        self.service = EquipamentService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_eq_equipament_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_eq_module_name"
        context["titleForm"] = "gc_eq_equipament_title_form"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("gc:eq:listing-equipament")
        context["urlForm"] = reverse_lazy("gc:eq:create-equipament")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

    @method_decorator(csrf_protect)
    def post(self, request, *arg, **kwargs):
        print(request.headers.get("x-requested-with"))
        print(request.headers.get("X-Requested-With"))
        if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
            try:
                self.service.creator(self.get_form(), request)
                return JsonResponse({"message": f"Se ha registro {request.POST['name']} con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message.replace("'", '"'))})

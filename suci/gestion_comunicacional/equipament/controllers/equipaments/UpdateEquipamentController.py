import json

from gestion_comunicacional.equipament.forms.EquipamentForm import EquipamentForm
from gestion_comunicacional.equipament.services.EquipamentService import EquipamentService
from templates.sneat import TemplateLayout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView


class UpdateEquipament(LoginRequiredMixin, UpdateView):
    form_class = EquipamentForm
    template_name = "gc/equipaments/equipaments/update.html"

    def __init__(self):
        self.service = EquipamentService()

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, **kwargs):
        pk = self.kwargs.get("pk")

        if pk:
            try:
                data = self.service.reader(pk)
                data.updated_by = self.request.user
                return data
            except Http404:
                raise Http404("El recurso no se ha encontrada")
        else:
            raise Http404("No se proporcionó ningún recurso válido")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_eq_equipament_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_eq_module_name"
        context["titleForm"] = "gc_eq_equipament_title_form"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("gc:eq:listing-equipament")
        context["urlForm"] = reverse_lazy("gc:eq:updater-equipament", args=[self.kwargs.get("pk")])
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

    def post(self, request, pk, *arg, **kwargs):
        if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
            try:
                self.service.updater(self.get_object(), self.get_form())
                return JsonResponse({"message": "Se ha acrualizado con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message)})

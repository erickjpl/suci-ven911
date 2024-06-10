import datetime
import json

from gestion_comunicacional.equipments.services.EquipmentService import EquipmentService
from templates.sneat import TemplateLayout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView


class DeleteEquipment(LoginRequiredMixin, DeleteView):
    template_name = "gc/equipments/equipments/delete.html"

    def __init__(self):
        self.service = EquipmentService()

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, **kwargs):
        pk = self.kwargs.get("pk")

        if pk:
            try:
                data = self.service.reader(pk)
                data.updated_by = self.request.user
                data.deleted_by = self.request.user
                data.deleted_at = datetime.datetime.now()
                return data
            except Http404:
                raise Http404("El recurso no se ha encontrada")
        else:
            raise Http404("No se proporcionó ningún recurso válido")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_eq_equipments_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_eq_module_name"
        context["titleForm"] = "gc_eq_equipments_title_form"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("gc:eq:listing-equipments")
        context["urlDelete"] = reverse_lazy("gc:eq:destroyer-equipments", args=[self.kwargs.get("pk")])
        return TemplateLayout.init(self, context)

    def delete(self, request, pk, *arg, **kwargs):
        if request.method == "DELETE" and request.headers.get("x-requested-with") == "XMLHttpRequest":
            try:
                self.service.destroyer(self.get_object())
                return JsonResponse({"message": "Se ha acrualizado con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message)})

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from gestion_comunicacional.equipament.forms.EquipamentForm import EquipamentForm
from gestion_comunicacional.equipament.services.EquipamentService import (
    EquipamentService,
)
from templates.sneat import TemplateLayout


class CreateEquipament(LoginRequiredMixin, CreateView):
    template_name = "gc/equipaments/equipaments/create.html"
    form_class = EquipamentForm
    success_url = reverse_lazy("gc:eq:listing-equipament")

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
        return TemplateLayout.init(self, context)

    def post(self, request, *arg, **kwargs):
        try:
            self.service.creator(request)
            return HttpResponseRedirect(self.success_url)
        except ValidationError as e:
            print("HOLA")
            print(e)

        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = e

        return render(request, self.template_name, context)

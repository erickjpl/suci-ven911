from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from gestion_comunicacional.equipament.forms.EquipamentForm import EquipamentForm
from gestion_comunicacional.equipament.services.EquipamentService import (
    EquipamentService,
)
from templates.sneat import TemplateLayout


class EquipamentView(LoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        return TemplateLayout.init(self, super().get_context_data(**kwargs))


class ListEquipament(LoginRequiredMixin, ListView):
    template_name = "gc/equipament/listing-equipaments.html"
    context_object_name = "equipaments"

    def __init__(self):
        self.service = EquipamentService()

    @method_decorator(csrf_protect)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        page = self.request.GET.get("page") or 1
        search = self.request.GET.get("search") or None

        return self.service.getAll(page, search)

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            data = []
            for item in self.get_queryset():
                data.append(item.toJSON())
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)


class CreateEquipament(LoginRequiredMixin, CreateView):
    template_name = "gc/equipament/create.html"
    form_class = EquipamentForm
    success_url = reverse_lazy("gc:eq:listing-equipament")

    def __init__(self):
        self.service = EquipamentService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registro de equipos para el departamento"
        context["tag"] = "Asignar"

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
        # context["form"] = e

        return render(request, self.template_name, context)


class ReadEquipament(LoginRequiredMixin, DetailView):
    template_name = "gc/equipament.html"

    def __init__(self):
        self.service = EquipamentService()

    def get(self, request, pk):
        entity = self.service.getById(pk)

        if not entity:
            return HttpResponse(status=404)

        return render(request, self.template_name, {"entity": entity})


class UpdateEquipament(LoginRequiredMixin, UpdateView):
    template_name = "gc/equipament.html"

    def __init__(self):
        self.service = EquipamentService()

    def post(self, request, pk):
        entity = self.service.updater(request.PUT, pk)

        return render(request, self.template_name, {"entity": entity})


class DeleteEquipament(LoginRequiredMixin, DeleteView):
    template_name = "gc/equipament.html"

    def __init__(self):
        self.service = EquipamentService()

    def post(self, request, pk):
        entity = self.service.destroyer(pk)

        return render(request, self.template_name, {"entity": entity})

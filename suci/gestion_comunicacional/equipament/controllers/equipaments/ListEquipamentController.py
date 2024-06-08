from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from gestion_comunicacional.equipament.services.EquipamentService import EquipamentService
from templates.sneat import TemplateLayout


class ListEquipament(LoginRequiredMixin, ListView):
    template_name = "gc/equipaments/equipaments/listing.html"

    def __init__(self):
        self.service = EquipamentService()

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_eq_equipament_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_eq_module_name"
        context["createBtn"] = "gc_eq_equipament_title_btn_add"
        context["createUrl"] = reverse_lazy("gc:eq:create-equipament")
        context["listUrl"] = reverse_lazy("gc:eq:listing-equipament")
        context["updateUrl"] = reverse_lazy("gc:eq:updater-equipament", args=[0])
        context["deleteUrl"] = reverse_lazy("gc:eq:destroyer-equipament", args=[0])
        context["columns"] = "id|name|description|status"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        page = self.request.GET.get("page") or 1
        search = self.request.GET.get("search") or None

        return self.service.getAll(page, search)

    def get(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            data = {}
            try:
                data = []
                for item in self.get_queryset():
                    data.append(item.toJSON())
            except Exception as e:
                data["error"] = str(e)
            return JsonResponse(data, safe=False)

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

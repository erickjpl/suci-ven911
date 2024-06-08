from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from gestion_comunicacional.equipament.services.EquipamentService import EquipamentService


class ReadEquipament(LoginRequiredMixin, DetailView):
    template_name = "gc/equipament.html"

    def __init__(self):
        self.service = EquipamentService()

    def get(self, request, pk):
        entity = self.service.getById(pk)

        if not entity:
            return HttpResponse(status=404)

        return render(request, self.template_name, {"entity": entity})

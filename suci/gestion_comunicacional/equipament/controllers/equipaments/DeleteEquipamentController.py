from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DeleteView
from gestion_comunicacional.equipament.services.EquipamentService import (
    EquipamentService,
)


class DeleteEquipament(LoginRequiredMixin, DeleteView):
    template_name = "gc/equipament.html"

    def __init__(self):
        self.service = EquipamentService()

    def post(self, request, pk):
        entity = self.service.destroyer(pk)

        return render(request, self.template_name, {"entity": entity})

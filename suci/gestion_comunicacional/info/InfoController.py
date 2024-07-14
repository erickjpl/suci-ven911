from gestion_comunicacional.info.InfoService import InfoService

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class InfoController(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mainContentHeaderTitle"] = "Gestion Comunicacional"
        context["urlIfoApi"] = reverse_lazy("api-gc:info")
        return context


class InfoControllerApi(LoginRequiredMixin, TemplateView):
    def __init__(self):
        self.service = InfoService()

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            data = self.service.info()
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

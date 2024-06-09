import json

from gestion_comunicacional.social_activity.forms.SocialActivityForm import SocialActivityForm
from gestion_comunicacional.social_activity.services.SocialActivityService import SocialActivityService
from templates.sneat import TemplateLayout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView


class UpdateSocialActivity(LoginRequiredMixin, UpdateView):
    template_name = "gc/social-activity/update.html"
    form_class = SocialActivityForm

    def __init__(self):
        self.service = SocialActivityService()

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
        context["titlePage"] = "gc_sa_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_sa_module_name"
        context["titleForm"] = "gc_sa_title_form"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("gc:sa:listing-activity")
        context["urlForm"] = reverse_lazy("gc:sa:updater-activity", args=[self.kwargs.get("pk")])
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

    def post(self, request, pk, *arg, **kwargs):
        if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
            try:
                self.service.updater(self.get_object(), self.get_form())
                return JsonResponse({"message": "Se ha acrualizado con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message)})

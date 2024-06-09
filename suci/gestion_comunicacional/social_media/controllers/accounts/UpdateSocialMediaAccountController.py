import json

from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity
from gestion_comunicacional.social_media.forms.SocialMediaAccountForm import SocialMediaAccountForm
from gestion_comunicacional.social_media.services.SocialMediaAccountService import SocialMediaAccountService
from templates.sneat import TemplateLayout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import UpdateView


class UpdateSocialMediaAccount(LoginRequiredMixin, UpdateView):
    form_class = SocialMediaAccountForm
    template_name = "gc/social-media/accounts/update.html"

    def __init__(self):
        self.service = SocialMediaAccountService()

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateSocialMediaAccount, self).dispatch(request, *args, **kwargs)

    def get_object(self, **kwargs):
        pk = self.kwargs.get("pk")

        if pk:
            try:
                data = self.service.reader(pk)
                data.updated_by = self.request.user
                return data
            except Http404:
                raise Http404("La cuenta de la red social no se ha encontrada")
        else:
            raise Http404("No se proporcionó ningún recurso válido")

    # def get_form(self):
    #     self.form_class(self.object, self.request.POST)
    #     return super().get_form()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_sm_account_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_sm_module_name"
        context["titleForm"] = "gc_sm_account_title_form"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("gc:sm:listing-account")
        context["urlForm"] = reverse_lazy("gc:sm:updater-account", args=[self.kwargs.get("pk")])
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

    @method_decorator(csrf_protect)
    def post(self, request, pk, *arg, **kwargs):
        if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
            try:
                self.service.updater(self.get_object(), self.get_form())
                return JsonResponse({"message": f"Se ha acrualizado {request.POST['username_sm']} con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message)})

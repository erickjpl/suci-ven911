from gestion_comunicacional.mixins.CheckPermisosMixin import CheckPermisosMixin
from gestion_comunicacional.mixins.ControllerMixin import UpdateController
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity
from gestion_comunicacional.social_media.forms.SocialMediaAccountForm import SocialMediaAccountForm
from gestion_comunicacional.social_media.services.SocialMediaAccountService import SocialMediaAccountService

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class UpdateSocialMediaAccount(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = SocialMediaAccountEntity.CHANGE_SOCIAL_MEDIA

    def get(self, request, *arg, **kwargs):
        context = {}
        context["modalTitle"] = "Editar Red Social"
        context["urlApi"] = reverse_lazy("api-gc:sm:update-account", args=[self.kwargs.get("pk")])
        context["methodForm"] = "PUT"
        return JsonResponse(context)


class UpdateSocialMediaAccountApi(UpdateController, CheckPermisosMixin):
    form_class = SocialMediaAccountForm
    redirect_not_found = reverse_lazy("gc:sm:list-account")
    permission_required = SocialMediaAccountEntity.CHANGE_SOCIAL_MEDIA

    def __init__(self):
        self.service = SocialMediaAccountService()

from gestion_comunicacional.mixins.CheckPermisosMixin import CheckPermisosMixin
from gestion_comunicacional.mixins.ControllerMixin import DeleteController
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity
from gestion_comunicacional.social_media.services.SocialMediaAccountService import SocialMediaAccountService

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class DeleteSocialMediaAccount(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = SocialMediaAccountEntity.DELETE_SOCIAL_MEDIA

    def get(self, request, *arg, **kwargs):
        context = {}
        context["modalTitle"] = "Eliminando, Red Social..!"
        context["urlApi"] = reverse_lazy("api-gc:sm:delete-account", args=[self.kwargs.get("pk")])
        context["methodForm"] = "DELETE"
        return JsonResponse(context)


class DeleteSocialMediaAccountApi(DeleteController, CheckPermisosMixin):
    redirect_not_found = reverse_lazy("gc:sm:list-account")
    permission_required = SocialMediaAccountEntity.DELETE_SOCIAL_MEDIA

    def __init__(self):
        self.service = SocialMediaAccountService()

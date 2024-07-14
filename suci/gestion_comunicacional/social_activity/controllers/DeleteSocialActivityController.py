from gestion_comunicacional.mixins.CheckPermisosMixin import CheckPermisosMixin
from gestion_comunicacional.mixins.ControllerMixin import DeleteController
from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity
from gestion_comunicacional.social_activity.services.SocialActivityService import SocialActivityService

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class DeleteSocialActivity(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = SocialActivityEntity.DELETE_SOCIAL_ACTIVITY

    def get(self, request, *arg, **kwargs):
        context = {}
        context["modalTitle"] = "Eliminando, Actividad Social..!"
        context["urlApi"] = reverse_lazy("api-gc:sa:delete-activity", args=[self.kwargs.get("pk")])
        context["methodForm"] = "DELETE"
        return JsonResponse(context)


class DeleteSocialActivityApi(DeleteController, CheckPermisosMixin):
    redirect_not_found = reverse_lazy("gc:sa:list-activity")
    permission_required = SocialActivityEntity.DELETE_SOCIAL_ACTIVITY

    def __init__(self):
        self.service = SocialActivityService()

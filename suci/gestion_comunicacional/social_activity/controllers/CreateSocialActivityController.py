from gestion_comunicacional.mixins.CheckPermisosMixin import CheckPermisosMixin
from gestion_comunicacional.mixins.ControllerMixin import CreateController
from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity
from gestion_comunicacional.social_activity.forms.SocialActivityForm import SocialActivityForm
from gestion_comunicacional.social_activity.services.SocialActivityService import SocialActivityService

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class CreateSocialActivity(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    form_class = SocialActivityForm
    permission_required = SocialActivityEntity.ADD_SOCIAL_ACTIVITY

    def get(self, request, *arg, **kwargs):
        context = {}
        context["modalTitle"] = "Registrar una Actividad Social"
        context["urlApi"] = reverse_lazy("api-gc:sa:create-activity")
        context["methodForm"] = "POST"
        return JsonResponse(context)


class CreateSocialActivityApi(CreateController, CheckPermisosMixin):
    template_name = "gc/social-activity/create.html"
    form_class = SocialActivityForm
    permission_required = SocialActivityEntity.ADD_SOCIAL_ACTIVITY

    def __init__(self):
        self.service = SocialActivityService()

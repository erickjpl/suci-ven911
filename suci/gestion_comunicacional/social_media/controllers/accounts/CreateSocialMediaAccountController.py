from gestion_comunicacional.mixins.CheckPermisosMixin import CheckPermisosMixin
from gestion_comunicacional.mixins.ControllerMixin import CreateController
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity
from gestion_comunicacional.social_media.forms.SocialMediaAccountForm import SocialMediaAccountForm
from gestion_comunicacional.social_media.services.SocialMediaAccountService import SocialMediaAccountService

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class CreateSocialMediaAccount(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    form_class = SocialMediaAccountForm
    permission_required = SocialMediaAccountEntity.ADD_SOCIAL_MEDIA

    def get(self, request, *arg, **kwargs):
        context = {}
        context["modalTitle"] = "Registrar Red Social"
        context["urlApi"] = reverse_lazy("api-gc:sm:create-account")
        context["methodForm"] = "POST"
        return JsonResponse(context)


class CreateSocialMediaAccountApi(CreateController, CheckPermisosMixin):
    template_name = "gc/social-media/accounts/create.html"
    form_class = SocialMediaAccountForm
    permission_required = SocialMediaAccountEntity.ADD_SOCIAL_MEDIA

    def __init__(self):
        self.service = SocialMediaAccountService()

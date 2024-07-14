import json

from gestion_comunicacional.mixins.CheckPermisosMixin import CheckPermisosMixin
from gestion_comunicacional.mixins.ControllerMixin import ListController
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity
from gestion_comunicacional.social_media.services.SocialMediaAccountService import SocialMediaAccountService

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView


class ListSocialMediaAccount(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    template_name = "modules.html"
    permission_required = SocialMediaAccountEntity.VIEW_SOCIAL_MEDIA

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Redes Sociales"
        context["mainContentHeaderTitle"] = "Gestion Comunicacional / Redes Sociales"
        context["form"] = 'social-media'
        context["listUrl"] = reverse_lazy("api-gc:sm:list-account")
        context["createUrl"] = reverse_lazy("gc:sm:create-account")
        context["updateUrl"] = reverse_lazy("gc:sm:update-account", args=[0])
        context["deleteUrl"] = reverse_lazy("gc:sm:delete-account", args=[0])
        columns = [
            {"data": "id", "name": "id", "title": "ID", "orderable": "false", "searchable": "false"},
            {"data": "platform", "name": "platform", "title": "Red Social", "orderable": "false", "searchable": "false"},
            {"data": "username_sm", "name": "username_sm", "title": "Usuario", "orderable": "false", "searchable": "false"},
            {"data": "followers", "name": "followers", "title": "Seguidores", "orderable": "false", "searchable": "false"},
            {"data": "responsible", "name": "responsible", "title": "Responsable", "orderable": "false", "searchable": "false"},
            {"data": "publications", "name": "publications", "title": "Publicaciones", "orderable": "false", "searchable": "false"},
            {"title": "Acciones"},
        ]
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return context
      


class ListSocialMediaAccountApi(ListController, CheckPermisosMixin):
    permission_required = SocialMediaAccountEntity.VIEW_SOCIAL_MEDIA

    def __init__(self):
        self.service = SocialMediaAccountService()

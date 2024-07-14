import json

from gestion_comunicacional.mixins.CheckPermisosMixin import CheckPermisosMixin
from gestion_comunicacional.mixins.ControllerMixin import ListController
from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity
from gestion_comunicacional.social_activity.services.SocialActivityService import SocialActivityService

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView


class ListSocialActivity(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    template_name = "modules.html"
    permission_required = SocialActivityEntity.VIEW_SOCIAL_ACTIVITY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actividades Sociales"
        context["mainContentHeaderTitle"] = "Gestion Comunicacional / Actividades Sociales"
        context["form"] = 'social-activity'
        context["listUrl"] = reverse_lazy("api-gc:sa:list-activity")
        context["createUrl"] = reverse_lazy("gc:sa:create-activity")
        context["updateUrl"] = reverse_lazy("gc:sa:update-activity", args=[0])
        context["deleteUrl"] = reverse_lazy("gc:sa:delete-activity", args=[0])
        columns = [
            {"data": "id", "name": "id", "title": "ID", "orderable": "false", "searchable": "false"},
            {"data": "date", "name": "date", "title": "Fecha y hora", "orderable": "false", "searchable": "false"},
            {"data": "activity_type", "name": "activity_type", "title": "Tipo de Actividad", "orderable": "false", "searchable": "false"},
            {"data": "reason", "name": "reason", "title": "Motivo", "orderable": "false", "searchable": "false"},
            {"data": "beneficiaries", "name": "beneficiaries", "title": "Beneficiarios", "orderable": "false", "searchable": "false"},
            {"title": "Acciones"},
        ]
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return context


class ListSocialActivityApi(ListController, CheckPermisosMixin):
    permission_required = SocialActivityEntity.VIEW_SOCIAL_ACTIVITY

    def __init__(self):
        self.service = SocialActivityService()

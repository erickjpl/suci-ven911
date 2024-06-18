from gestion_comunicacional.social_activity.services.SocialActivityService import SocialActivityService
from index.mixins.CheckPermisosMixin import CheckPermisosMixin
from index.mixins.ControllerMixin import ListController
from templates.sneat import TemplateLayout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class ListSocialActivityView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    template_name = "gc/social-activity/listing.html"
    permission_required = "gc.view_social_activity"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_sa_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_sa_module_name"
        context["createBtn"] = "gc_sa_title_btn_add"
        context["createUrl"] = reverse_lazy("gc:sa:create-activity")
        context["listUrl"] = reverse_lazy("gc:sa:api-listing-activity")
        context["updateUrl"] = reverse_lazy("gc:sa:updater-activity", args=[0])
        context["deleteUrl"] = reverse_lazy("gc:sa:destroyer-activity", args=[0])
        context["columns"] = "id|date|activity_type|location|reason|description|beneficiaries"
        return TemplateLayout.init(self, context)


class ListSocialActivity(ListController):
    permission_required = "gc.view_social_activity"

    def __init__(self):
        self.service = SocialActivityService()

from gestion_comunicacional.social_media.forms.SocialMediaAccountForm import SocialMediaAccountForm
from gestion_comunicacional.social_media.services.SocialMediaAccountService import SocialMediaAccountService
from index.mixins.ControllerMixin import CreateController
from templates.sneat import TemplateLayout

from django.urls import reverse_lazy


class CreateSocialMediaAccount(CreateController):
    form_class = SocialMediaAccountForm
    template_name = "gc/social-media/accounts/create.html"

    def __init__(self):
        self.service = SocialMediaAccountService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_sm_account_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_sm_module_name"
        context["titleForm"] = "gc_sm_account_title_form"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("gc:sm:listing-account")
        context["urlForm"] = reverse_lazy("gc:sm:create-account")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)
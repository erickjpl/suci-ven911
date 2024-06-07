from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from gestion_comunicacional.social_media.forms.SocialMediaAccountForm import (
    SocialMediaAccountForm,
)
from gestion_comunicacional.social_media.services.SocialMediaAccountService import (
    SocialMediaAccountService,
)
from templates.sneat import TemplateLayout


class CreateSocialMediaAccount(LoginRequiredMixin, CreateView):
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
        return TemplateLayout.init(self, context)

    def post(self, request, *arg, **kwargs):
        try:
            self.service.creator(request)
            return HttpResponseRedirect(self.success_url)
        except ValidationError as e:
            self.object = None
            context = self.get_context_data(**kwargs)
            context["form"] = e.message
            return render(request, self.template_name, context)

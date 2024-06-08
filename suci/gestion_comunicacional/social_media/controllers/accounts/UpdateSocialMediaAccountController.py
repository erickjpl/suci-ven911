from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import UpdateView

from gestion_comunicacional.social_media.forms.SocialMediaAccountForm import SocialMediaAccountForm
from gestion_comunicacional.social_media.services.SocialMediaAccountService import SocialMediaAccountService
from templates.sneat import TemplateLayout


class UpdateSocialMediaAccount(LoginRequiredMixin, UpdateView):
    form_class = SocialMediaAccountForm
    template_name = "gc/social-media/accounts/update.html"

    def __init__(self):
        self.service = SocialMediaAccountService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cuentas de redes sociales"
        context["tag"] = "Registrar"

        return TemplateLayout.init(self, context)

    def post(self, request, pk, *arg, **kwargs):
        try:
            self.service.updater(request, pk)(request)
            return HttpResponseRedirect(self.success_url)
        except ValidationError as e:
            self.object = None
            context = self.get_context_data(**kwargs)
            context["form"] = e.message
            return render(request, self.template_name, context)

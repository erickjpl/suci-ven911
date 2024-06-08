from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView

from gestion_comunicacional.social_media.services.SocialMediaAccountService import SocialMediaAccountService


class ReadSocialMediaAccount(LoginRequiredMixin, DetailView):
    template_name = "gc/social-media-account.html"

    def __init__(self):
        self.service = SocialMediaAccountService()

    def get(self, request, pk):
        entity = self.service.getById(pk)

        if not entity:
            return HttpResponse(status=404)

        return render(request, self.template_name, {"entity": entity})


class UpdateSocialMediaAccount(LoginRequiredMixin, UpdateView):
    template_name = "gc/social-media-account.html"

    def __init__(self):
        self.service = SocialMediaAccountService()

    def post(self, request, pk):
        entity = self.service.updater(request.PUT, pk)

        return render(request, self.template_name, {"entity": entity})


class DeleteSocialMediaAccount(LoginRequiredMixin, DeleteView):
    template_name = "gc/social-media-account.html"

    def __init__(self):
        self.service = SocialMediaAccountService()

    def post(self, request, pk):
        entity = self.service.destroyer(pk)

        return render(request, self.template_name, {"entity": entity})

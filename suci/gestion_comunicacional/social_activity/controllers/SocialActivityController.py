from gestion_comunicacional.social_activity.services.SocialActivityService import SocialActivityService
from templates.sneat import TemplateLayout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DeleteView, DetailView, ListView, UpdateView


class ReadSocialActivity(LoginRequiredMixin, DetailView):
    template_name = "gc/social-activity.html"

    def __init__(self):
        self.service = SocialActivityService()

    def get(self, request, pk):
        entity = self.service.getById(pk)

        if not entity:
            return HttpResponse(status=404)

        return render(request, self.template_name, {"entity": entity})


class UpdateSocialActivity(LoginRequiredMixin, UpdateView):
    template_name = "gc/social-activity.html"

    def __init__(self):
        self.service = SocialActivityService()

    def post(self, request, pk):
        entity = self.service.updater(request.PUT, pk)

        return render(request, self.template_name, {"entity": entity})


class DeleteSocialActivity(LoginRequiredMixin, DeleteView):
    template_name = "gc/social-activity.html"

    def __init__(self):
        self.service = SocialActivityService()

    def post(self, request, pk):
        entity = self.service.destroyer(pk)

        return render(request, self.template_name, {"entity": entity})

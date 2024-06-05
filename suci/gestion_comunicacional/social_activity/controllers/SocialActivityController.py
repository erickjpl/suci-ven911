from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from gestion_comunicacional.social_activity.services.SocialActivityService import (
    SocialActivityService,
)
from templates.sneat import TemplateLayout


class ListSocialActivity(LoginRequiredMixin, ListView):
    template_name = "gc/social-activity/listing-activities.html"
    context_object_name = "socialActivities"

    def __init__(self):
        self.service = SocialActivityService()

    def get_context_data(self, **kwargs):
        return TemplateLayout.init(self, super().get_context_data(**kwargs))

    def get_queryset(self):
        page = self.request.GET.get("page") or 1
        search = self.request.GET.get("search") or None

        return self.service.getAll(page, search)


class CreateSocialActivity(LoginRequiredMixin, CreateView):
    template_name = "gc/social-activity.html"

    def __init__(self):
        self.service = SocialActivityService()

    def post(self, request):
        entity = self.service.creator(request.POST)

        return render(request, self.template_name, {"entity": entity})


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

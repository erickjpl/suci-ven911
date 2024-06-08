from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView
from gestion_comunicacional.social_activity.services.SocialActivityService import SocialActivityService


class CreateSocialActivity(LoginRequiredMixin, CreateView):
    template_name = "gc/social-activity.html"

    def __init__(self):
        self.service = SocialActivityService()

    def post(self, request):
        entity = self.service.creator(request.POST)

        return render(request, self.template_name, {"entity": entity})

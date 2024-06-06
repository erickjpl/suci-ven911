from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from gestion_comunicacional.social_media.services.SocialMediaAccountService import (
    SocialMediaAccountService,
)
from templates.sneat import TemplateLayout


class ListSocialMediaAccount(LoginRequiredMixin, ListView):
    # class ListSocialMediaAccount(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    #     permission_required = "gc.equipament.view_logentry"
    template_name = "gc/social-media/listing.html"
    context_object_name = "accounts"

    def __init__(self):
        self.service = SocialMediaAccountService()

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        return TemplateLayout.init(self, super().get_context_data(**kwargs))

    def get_queryset(self):
        page = self.request.GET.get("page") or 1
        search = self.request.GET.get("search") or None

        return self.service.getAll(page, search)

    def get(self, request, *args, **kwargs):
        print(request.headers.get("x-requested-with"))
        if request.headers.get("x-requested-with"):
            data = {}
            try:
                data = []
                for item in self.get_queryset():
                    data.append(item.toJSON())
            except Exception as e:
                data["error"] = str(e)
            return JsonResponse(data, safe=False)

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


class CreateSocialMediaAccount(LoginRequiredMixin, CreateView):
    template_name = "gc/social-media-account.html"

    def __init__(self):
        self.service = SocialMediaAccountService()

    def post(self, request):
        entity = self.service.creator(request.POST)

        return render(request, self.template_name, {"entity": entity})


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

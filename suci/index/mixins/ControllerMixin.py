import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import error
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import Http404, HttpResponseRedirect, JsonResponse, QueryDict
from django.views.generic import CreateView, DeleteView, UpdateView


class CreateController(LoginRequiredMixin, CreateView):
    def post(self, request, *arg, **kwargs):
        if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
            try:
                self.service.creator(self.get_form(), request)
                return JsonResponse({"message": "Se ha registrado con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message.replace("'", '"'))})


class UpdateController(LoginRequiredMixin, UpdateView):
    redirect_not_found = None

    def dispatch(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Exception:
            return HttpResponseRedirect(self.redirect_not_found)

        if self.request.method.upper() == "PUT":
            return self.put(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, **kwargs):
        pk = self.kwargs.get("pk")

        if pk:
            try:
                data = self.service.reader(pk)
                data.updated_by = self.request.user
                return data
            except ObjectDoesNotExist:
                error(self.request, "El recurso no se ha encontrado")
        else:
            error(self.request, "No se proporcionó ningún recurso válido")

    def get_form(self):
        return self.form_class(QueryDict(self.request.body) or None, instance=self.get_object())

    def put(self, request, *arg, **kwargs):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            try:
                self.service.updater(self.get_object(), self.get_form())
                return JsonResponse({"message": "Se ha actualizado con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message)})


class DeleteController(LoginRequiredMixin, DeleteView):
    redirect_not_found = None

    def dispatch(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Exception:
            return HttpResponseRedirect(self.redirect_not_found)

        return super().dispatch(request, *args, **kwargs)

    def get_object(self, **kwargs):
        pk = self.kwargs.get("pk")

        if pk:
            try:
                data = self.service.reader(pk)
                data.updated_by = self.request.user
                data.deleted_by = self.request.user
                return data
            except ObjectDoesNotExist:
                error(self.request, "El recurso no se ha encontrado")
        else:
            error(self.request, "No se proporcionó ningún recurso válido")

    def delete(self, request, pk, *arg, **kwargs):
        if request.method == "DELETE" and request.headers.get("x-requested-with") == "XMLHttpRequest":
            try:
                self.service.destroyer(self.get_object())
                return JsonResponse({"message": "Se ha eliminado con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message)})

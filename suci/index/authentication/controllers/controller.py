from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from index.authentication.forms import LoginForm
from templates.sneat import TemplateLayout
from templates.sneat.helpers.theme import TemplateHelper


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("auth:login")


class AuthView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {"layout_path": TemplateHelper.set_layout("layout_blank.html", context)}
        )
        return context

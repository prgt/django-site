from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, Http404, render
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import Permission, User
from django.utils import timezone
from django.views import generic

from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.base import View, TemplateView

def home(request):
    return render(request, 'test1/home.html')

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


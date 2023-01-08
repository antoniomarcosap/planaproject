from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'account/home.html'


def RegisterView(request):
    pass


def LoginView(request):
    pass


def LogoutView(request):
    pass

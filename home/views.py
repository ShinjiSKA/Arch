from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_content = {'today': datetime.today()}


class AuthorizedView(TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

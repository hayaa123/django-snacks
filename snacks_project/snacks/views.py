from django.shortcuts import render
from django.views.generic import TemplateView

from snacks_project.settings import TEMPLATES
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

class AboutUsViews(TemplateView):
    template_name = "About_us.html"
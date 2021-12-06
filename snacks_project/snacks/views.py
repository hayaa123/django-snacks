from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from django.views.generic.detail import DetailView
from .models import Snack
from snacks_project.settings import TEMPLATES
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

class AboutUsViews(TemplateView):
    template_name = "About_us.html"

class SnackListView(ListView):
    template_name = "snack_list.html"
    model =  Snack

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack
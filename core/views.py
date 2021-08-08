from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'core/index.html'



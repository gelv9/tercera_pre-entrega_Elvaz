from django.shortcuts import render
from django.views.generic import ListView
from cursos.models import Curso
from django.views.generic import TemplateView

class ListaCursosView(ListView):
    model = Curso
    template_name = 'inicio/inicio.html'
    context_object_name = 'cursos'

def get_queryset(self):
    return Curso.objects.all()[:3]

class AboutView(TemplateView):
    template_name = "inicio/about.html"
from django.shortcuts import render
from django.views.generic import ListView
from cursos.models import Curso


class ListaCursosView(ListView):
    model = Curso
    template_name = 'inicio/inicio.html'
    context_object_name = 'cursos'
    
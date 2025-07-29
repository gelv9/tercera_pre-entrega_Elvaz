from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Curso

class AltaCursoView(UserPassesTestMixin, CreateView):
    model = Curso
    fields = ['titulo', 'materia', 'duracion', 'profesor']
    template_name = 'alta_curso.html'
    success_url = reverse_lazy('inicio:inicio')

    def test_func(self):
        return self.request.user.is_superuser

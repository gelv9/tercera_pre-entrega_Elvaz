from django.urls import path, include
from .views import AltaCursoView, ListaCompletaCursosView

app_name = 'cursos'

urlpatterns = [
    path('alta_curso/', AltaCursoView.as_view(), name='alta_curso'),
    path('lista/', ListaCompletaCursosView.as_view(), name='lista_cursos'),
]

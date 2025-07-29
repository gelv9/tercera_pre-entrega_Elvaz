from django.urls import path, include
from .views import AltaCursoView
urlpatterns = [
    path('alta_curso/', AltaCursoView.as_view(), name='alta_curso'),
    path('usuarios/', include('usuarios.urls')),
]

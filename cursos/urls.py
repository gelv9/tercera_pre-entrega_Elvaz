from django.urls import path, include
from . import views

urlpatterns = [
    path('alta_curso/', views.alta_curso, name='alta_curso'),
    path('usuarios/', include('usuarios.urls')),
]

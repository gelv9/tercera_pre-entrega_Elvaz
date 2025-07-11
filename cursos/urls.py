from django.urls import path
from . import views

urlpatterns = [
    path('alta_curso/', views.alta_curso, name='alta_curso'),
]

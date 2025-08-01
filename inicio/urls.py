from django.urls import path
from .views import ListaCursosView, AboutView

app_name = 'inicio'

urlpatterns = [
    path('', ListaCursosView.as_view(), name = 'inicio'),
    path('about/', AboutView.as_view(), name='about'),
]
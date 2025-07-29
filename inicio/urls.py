from django.urls import path
from .views import ListaCursosView

app_name = 'inicio'

urlpatterns = [
    path('', ListaCursosView.as_view(), name = 'inicio')
]
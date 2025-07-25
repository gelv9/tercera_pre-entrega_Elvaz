from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.registro, name='registro'),
]

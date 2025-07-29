from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from usuarios.forms import FormularioRegistro, FormularioEdicionPerfil
from django.contrib.auth.decorators import login_required
from usuarios.models import InfoExtra
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView

def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            InfoExtra.objects.get_or_create(user=usuario)
            return redirect('/')  # <- Asegurate que esta vista exista
    else:
        formulario = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'formulario': formulario})

def logout(request):
    django_logout(request)
    return render(request, 'usuarios/logout.html')

def registro(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect ("ususarios:login")
    else:
        formulario = FormularioRegistro()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

@login_required
def editar_perfil(request):
    info_extra = request.user.infoextra
    if request.method == "POST":
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            avatar = formulario.cleaned_data.get('avatar')
            info_extra.avatar = avatar if avatar else info_extra.avatar
            info_extra.save()
            formulario.save()
            return redirect("inicio:inicio")
        else:
            return render(request, 'usuarios/registro.html', {'formulario': formulario})
    else:
        formulario = FormularioEdicionPerfil(instance=request.user, initial={'avatar': info_extra.avatar})
        return render(request, 'usuarios/registro.html', {'formulario': formulario})

class CambioContrasenia(PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('inicio:inicio')
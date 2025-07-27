from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from usuarios.forms import FormularioRegistro

def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            django_login(request, user)
            return redirect('inicio')  # <- Asegurate que esta vista exista
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
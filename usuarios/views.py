from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login 


def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            django_login(request, user)
            ...
            return redirect('inicio')
    else:
        formulario = ...()
        
    return render(request, 'usuarios/login.html', {'formularios': formulario})

def logout(request):
    return render(request, 'usuarios/logout.html')

def registro(request):
    return render(request, 'usuarios/registro.html')
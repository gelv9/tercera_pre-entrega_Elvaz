from django.shortcuts import render, redirect
from .forms import CursoForm

def alta_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else: 
        form = CursoForm()
    return render(request, 'alta_curso.html', {'form':form})
    

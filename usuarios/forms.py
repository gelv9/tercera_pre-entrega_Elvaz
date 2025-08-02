from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import InfoExtra

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese una contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {key: '' for key in fields}

class FormularioEdicionPerfil(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        help_texts = {key: '' for key in fields}
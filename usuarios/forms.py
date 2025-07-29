from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class FormularioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        help_text = {key: '' for key in fields}
        
class FormularioEdicionPerfil():
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    password = None
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name','last_name', 'avatar']
        help_text = {key: '' for key in fields}
        
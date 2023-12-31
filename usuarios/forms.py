from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class RegistarseForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'telefono', 'domicilio', 'imagen_perfil']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name','email', 'telefono', 'domicilio', 'imagen_perfil']

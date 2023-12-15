from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistarseForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'telefono', 'domicilio']

       
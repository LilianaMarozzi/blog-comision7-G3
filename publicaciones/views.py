from django.shortcuts import render, redirect
from .models import Publicacion

# Views basada en funciones para enlistar las publicaciones
def publicaciones_view (request):

    ctx = {
        'publicaciones' : Publicacion.objects.all()
    }

    return render (request, 'publicaciones.html', ctx)    
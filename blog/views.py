from django.shortcuts import render
from publicaciones.models import Publicacion

def index_view (request):
    ctx = {
        'mejores_posteo' : Publicacion.objects.order_by('-me_gusta')[:3]
    }
    return render (request, 'index.html', ctx)

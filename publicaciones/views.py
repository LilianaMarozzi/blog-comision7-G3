from django.shortcuts import render, redirect
from .models import Publicacion
from django.views.generic import ListView
from .forms import PublicarForm

# Views basada en funciones para enlistar las publicaciones
def publicaciones_view (request):

    ctx = {
        'publicaciones' : Publicacion.objects.all(),
    }
    return render(request, 'publicaciones/publicaciones.html', ctx)   
 
 

#views basada en una fn para CREAR una publicacion
def publicar_view(request):
    if request.method == "POST":
        form= PublicarForm(request.POST)
        if form.is_valid():
            nueva_publicacion = form.save()
            return redirect ('publicaciones')
    else:
        form = PublicarForm()
        ctx = {'form' : form}
        return render(request, 'publicaciones/publicar.html', ctx)
    
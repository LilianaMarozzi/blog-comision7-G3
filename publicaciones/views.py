from django.shortcuts import render
from .models import Publicacion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import PublicarForm
"""
# Views basada en funciones para enlistar las publicaciones
def publicaciones_view (request):

    ctx = {
        'publicaciones' : Publicacion.objects.all()
    }

    return render (request, 'publicaciones.html', ctx)    
"""
# View basada en clase para ENLISTAR publicaciones
class PublicacionesView(ListView):
    model = Publicacion
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'publicaciones'

# View basada en clase para CREAR publicaciones
class PublicarView(CreateView):
    model = Publicacion
    template_name = 'publicaciones/publicar.html'
    form_class = PublicarForm

class ModificarPublicacionView(UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = PublicarForm
    success_url = '../ver-publicaciones'
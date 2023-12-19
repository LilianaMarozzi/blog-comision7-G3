from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Publicacion, Comentario
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import PublicarForm, ComentarioForm


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

    def form_valid(self, form):
        f = form.save(commit=False)
        f.creador_id = self.request.user.id
        return super().form_valid(f)
    
    def get_success_url(self):
        return reverse('publicaciones')

# View basada en clase para MODIFICAR publicaciones
class ModificarPublicacionView(UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = PublicarForm
    success_url = '../ver-publicaciones'

# View basada en clase para ELIMINAR publicaciones
class EliminarPublicacionView(DeleteView):
    model = Publicacion
    template_name = 'publicaciones/eliminar-publicacion.html'
    success_url = '../ver-publicaciones'

#View para ver en detalle UNA PUBLICACION
    
class DetallePublicacion(DetailView):
    model= Publicacion
    template_name= 'publicaciones/detalle.html'
    context_object_name= 'publicacion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context
    
    def post(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated:
            return redirect('login')

        publicacion = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit= False)
            comentario.creador_id = self.request.user.id
            comentario.publicacion = publicacion
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)


class BorrarComentarioView(DeleteView):
    template_name= 'comentarios/borrar-comentario.html'
    model= Comentario

    def get_success_url(self):
        return reverse('detalle-publicacion', args=[self.object.publicacion.id])
    

class EditarComentarioView(UpdateView):
    template_name = 'comentarios/editar-comentario.html'
    model= Comentario
    form_class= ComentarioForm

    def get_success_url(self):
        return reverse('detalle-publicacion', args=[self.object.publicacion.id])
    


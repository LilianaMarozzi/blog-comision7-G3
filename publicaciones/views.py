from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Publicacion
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import PublicarForm


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
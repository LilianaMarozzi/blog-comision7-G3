from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion, Comentario, Categoria
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import PublicarForm, ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import ColaboradorMixin, CreadorMixin


# View basada en clase para ENLISTAR publicaciones
class PublicacionesView(ListView):
    model = Publicacion
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'publicaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publicaciones = context['publicaciones']
        for publicacion in publicaciones:
            publicacion.preview_truncada = publicacion.cuerpo[:160]
        return context 
    
    def get_queryset(self):
        queryset = super().get_queryset()

        #Filtrando por categoría
        categoria_seleccionada = self.request.GET.get('categoria')

        if categoria_seleccionada:
            queryset = queryset.filter(categoria = categoria_seleccionada)
        
        #orden
        orden = self.request.GET.get('orderby')
        if orden: 
            if orden == 'fecha_asc':
                queryset = queryset.order_by('fecha')
            elif orden == 'fecha_desc':
                queryset = queryset.order_by('-fecha')
            elif orden == 'alf_asc':
                queryset = queryset.order_by('titulo')
            elif orden == 'alf_desc':
                queryset = queryset.order_by('-titulo')
        
        return queryset

# View basada en clase para CREAR publicaciones
class PublicarView(LoginRequiredMixin, ColaboradorMixin, CreateView):
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
class ModificarPublicacionView(LoginRequiredMixin, CreadorMixin, UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = PublicarForm
    success_url = '../ver-publicaciones'

# View basada en clase para ELIMINAR publicaciones
class EliminarPublicacionView(LoginRequiredMixin, CreadorMixin, DeleteView):
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


class BorrarComentarioView(LoginRequiredMixin, CreadorMixin, DeleteView):
    template_name= 'comentarios/borrar-comentario.html'
    model= Comentario

    def get_success_url(self):
        return reverse('detalle-publicacion', args=[self.object.publicacion.id])
    

class EditarComentarioView(LoginRequiredMixin, CreadorMixin, UpdateView):
    template_name = 'comentarios/editar-comentario.html'
    model= Comentario
    form_class= ComentarioForm

    def get_success_url(self):
        return reverse('detalle-publicacion', args=[self.object.publicacion.id])
    

#Views para leer "acerca de"
def acerca_view(request):
    return render(request, 'acerca-de.html', {})

def me_gusta(request):
    if request.method == 'POST':
        publicacion_id = request.POST.get('publicacion_id')
        publicacion = get_object_or_404(Publicacion, id=publicacion_id)
        usuario = request.user

    if publicacion.me_gusta.filter(id=usuario.id).exists():
        publicacion.me_gusta.remove(usuario)
    else:
        publicacion.me_gusta.add(usuario)
    
    return redirect('publicaciones')
from django.shortcuts import render
from publicaciones.models import Publicacion
from publicaciones.views import PublicacionesView

class IndexView(PublicacionesView):
    model = Publicacion
    template_name = 'index.html'
    context_object_name = 'publicaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['mejores_posteo'] = Publicacion.objects.order_by('-me_gusta')[:3]

        publicaciones = context['mejores_posteo']
        for publicacion in publicaciones:
            publicacion.preview_truncada = publicacion.cuerpo[:160]

        return context
    
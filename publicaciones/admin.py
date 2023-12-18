from django.contrib import admin

from .models import Publicacion, Categoria


admin.site.register(Publicacion)
admin.site.register(Categoria)
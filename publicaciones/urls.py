from django.urls import path
from . import views


urlpatterns = [
    path("ver-publicaciones/", views.publicaciones_view, name="publicaciones"),
    path("publicar/", views.publicar_view, name="publicar")
]


from django.urls import path
from . import views


urlpatterns = [
    path('registrarse/', views.RegistrarseView.as_view(), name='registrarse')
]
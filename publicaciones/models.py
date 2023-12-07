from django.db import models

class Publicacion(models.Model):
    fecha= models.DateField(auto_now_add=True)
    titulo= models.CharField(max_length=50)
    cuerpo= models.TextField()
    categoria= models.CharField(max_length=50)
    creador= models.CharField(max_length=50)


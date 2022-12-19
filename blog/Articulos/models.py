from django.db import models

# Create your models here.
class Entrada (models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField(max_length=400)
    autor = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="media",null=True)

def __str__(self):
        return self.nombre
 
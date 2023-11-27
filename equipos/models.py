from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class equipos (models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=256)
    ubicacion = models.CharField(max_length=256)

def __str__(self):
    return f"{self.nombre} {self.ubicacion}"


class proveedores (models.Model):
    nombre = models.CharField(max_length=128)
    contacto = models.CharField(max_length=256)
    datos_adicionales = models.CharField(max_length=256)

class articulos(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    fecha = models.DateField(null=True, max_length=20)
    mensaje = models.TextField(null=True, blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
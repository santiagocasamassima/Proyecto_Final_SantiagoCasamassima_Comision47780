from django.db import models

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

class referentes (models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=128)
    interno = models.CharField(max_length=30)
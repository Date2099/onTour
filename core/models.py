from django.contrib.auth.models import User
from django.db import models

class Viaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    total_personas = models.IntegerField()
    def __str__(self):
        return self.nombre

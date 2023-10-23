from django.db import models

# Create your models here.

class Partido(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"Partido el {self.fecha} a las {self.hora}"
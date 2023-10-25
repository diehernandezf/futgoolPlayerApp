from django.db import models

class Calificacion(models.Model):
    valor = models.PositiveIntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    calificaciones = models.ManyToManyField(Calificacion, related_name='usuarios')

    def calcular_promedio(self):
        total_calificaciones = self.calificaciones.aggregate(models.Sum('valor'))['valor__sum']
        if total_calificaciones is None:
            return 0
        else:
            return total_calificaciones / self.calificaciones.count()

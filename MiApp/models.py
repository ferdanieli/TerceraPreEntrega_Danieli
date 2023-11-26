from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField(unique=True)

    def __str__(self):
        return f" {self.nombre} - Comisión: {self.comision}"


class Director(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f" {self.nombre} {self.apellido}"

class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    puntos = models.IntegerField()

    def __str__(self):
        return f" {self.nombre} - {self.puntos} puntos"

from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return f" {self.nombre}, comisión: {self.comision}"


class Director(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Director: {self.nombre} {self.apellido}"

class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    puntos = models.IntegerField()

    def __str__(self):
        return f"Materia: {self.nombre} {self.puntos}"

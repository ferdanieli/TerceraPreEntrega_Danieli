from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

class Director(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    puntos = models.IntegerField()

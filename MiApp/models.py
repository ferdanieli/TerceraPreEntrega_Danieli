from django.contrib.auth.models import User
from django.db import models
import datetime


class Carrera(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="carrera")
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
    comision = models.IntegerField(unique=True)

    def __str__(self):
        return f" {self.titulo} - Comisión: {self.comision}"


class Commentarios(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())


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

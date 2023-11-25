from django.shortcuts import render
from django.http import HttpResponse
from MiApp.models import Carrera

def crear_carrera(request):
    carrera = Carrera(nombre= "Logistica", comision= 12023)
    carrera.save()

    return HttpResponse(carrera.nombre)

from django.shortcuts import render
from django.http import HttpResponse
from MiApp.models import Carrera

def crear_carrera(request):
    carrera = Carrera(nombre= "Logistica", comision= 12023)
    carrera.save()
    contexto = {"carrera": carrera}

    return render(request, 'index.html', contexto)

def show_html(request):
    carrera = Carrera.objects.first()
    contexto = {"carrera": carrera}
    return render(request, 'index.html', contexto)

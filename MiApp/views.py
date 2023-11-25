from django.shortcuts import render, redirect
from MiApp.models import Carrera


def mostrar_carreras(request):
    carreras = Carrera.objects.all()
    contexto = {
        'carreras': carreras,

    }
    return render(request, 'MiApp/carreras.html', contexto)

def crear_carrera(request):
    carrera = Carrera(nombre= "Logistica", comision= 12023)
    carrera.save()

    return redirect("/app/carreras/")

def show_html(request):
    carrera = Carrera.objects.first()
    contexto = {"carrera": carrera}
    return render(request, 'index.html', contexto)

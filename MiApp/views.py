from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from MiApp.models import Carrera
from MiApp.forms import CarreraForm, BuscarCarreraForm


def mostrar_carreras(request):
    carreras = Carrera.objects.all()
    contexto = {
        "carreras": carreras,
        "form": BuscarCarreraForm(),
    }

    return render(request, 'MiApp/carreras.html', contexto)

def crear_carrera(request):
    carrera = Carrera(nombre= "Logistica", comision= 12023)
    carrera.save()

    return redirect("/app/carreras/")

def crear_carrera_form(request):

    if request.method == "POST":
        carrera_formulario = CarreraForm(request.POST)

        if carrera_formulario.is_valid():
            informacion = carrera_formulario.cleaned_data
            carrera_crear = Carrera(nombre=informacion["nombre"], comision=informacion["comisión"])
            carrera_crear.save()
            return redirect("/app/carreras/")

    carrera_formulario = CarreraForm()
    contexto = {
         "form": carrera_formulario
    }
    return render(request, "MiApp/crear_carrera.html", contexto)


def buscar_comision(request):
    try:
       nombre = request.GET["nombre"]
       carreras = Carrera.objects.filter(nombre__icontains=nombre)
       contexto = {
           "carreras": carreras,
           "form": BuscarCarreraForm(),
       }

       return render(request, "MiApp/carreras.html", contexto)

    except MultiValueDictKeyError:
        return redirect("/CoderApp/cursos/")

def show_html(request):
    carrera = Carrera.objects.first()
    contexto = {"carrera": carrera}
    return render(request, 'index.html', contexto)

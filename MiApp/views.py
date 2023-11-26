from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from MiApp.models import Carrera, Director, Materia
from MiApp.forms import CarreraForm, BuscarCarreraForm, DirectorForm, BuscarDirectorForm, MateriaForm, BuscarMateriaForm


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
        return redirect("/app/carreras/")

def crear_director(request):
    director = Director(nombre= "Pablo", apellido= "Perez", email= "pperez@instituto.edu.ar")
    director.save()

    return redirect("/app/directores/")

def ver_directores(request):
    directores = Director.objects.all()
    contexto = {
        "directores": directores,
        "form": BuscarDirectorForm(),
    }

    return render(request, 'MiApp/directores.html', contexto)

def director_form(request):
    if request.method == "POST":
        director_formulario = DirectorForm(request.POST)

        if director_formulario.is_valid():
            informacion = director_formulario.cleaned_data
            director_crear = Director(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            director_crear.save()
            return redirect("/app/directores/")

    director_formulario = DirectorForm()
    contexto = {
         "form": director_formulario
    }
    return render(request, "MiApp/crear_director.html", contexto)

def buscar_director(request):
    try:
       nombre = request.GET["nombre"]
       directores = Director.objects.filter(nombre__icontains=nombre)
       contexto = {
           "directores": directores,
           "form": BuscarDirectorForm(),
       }

       return render(request, "MiApp/directores.html", contexto)

    except MultiValueDictKeyError:
        return redirect("/app/directores/")

def crear_materia(request):
    materia = Materia(nombre= "Ofimática", puntos= "20")
    materia.save()

    return redirect("/app/materias/")

def ver_materias(request):
    materias = Materia.objects.all()
    contexto = {
        "materias": materias,
        "form": BuscarMateriaForm(),
    }

    return render(request, 'MiApp/materias.html', contexto)

def materia_form(request):
    if request.method == "POST":
        materia_formulario = MateriaForm(request.POST)

        if materia_formulario.is_valid():
            informacion = materia_formulario.cleaned_data
            materia_crear = Materia(nombre=informacion["nombre"], puntos=informacion["puntos"])
            materia_crear.save()
            return redirect("/app/materias/")

    materia_formulario = MateriaForm()
    contexto = {
         "form": materia_formulario
    }
    return render(request, "MiApp/crear_materia.html", contexto)

def buscar_materia(request):
    try:
       nombre = request.GET["nombre"]
       materias = Materia.objects.filter(nombre__icontains=nombre)
       contexto = {
           "materias": materias,
           "form": BuscarMateriaForm(),
       }

       return render(request, "MiApp/materias.html", contexto)

    except MultiValueDictKeyError:
        return redirect("/app/materias/")

def show_html(request):
    carrera = Carrera.objects.first()
    director = Director.objects.first()
    materia = Materia.objects.first()
    contexto = {"carrera": carrera, "director": director, "materia": materia}
    return render(request, 'index.html', contexto)
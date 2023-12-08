from django.urls import path
from MiApp.views import CrearCarrera, show_html, mostrar_carreras, crear_carrera_form, buscar_comision, ver_directores, \
    crear_director, director_form, buscar_director, crear_materia, materia_form, ver_materias, buscar_materia, \
    DetalleCarrera

urlpatterns = [
    path('crear/', CrearCarrera.as_view()),
    path('nuevo/', crear_director),
    path('nueva/', crear_materia),
    path('carrera/', crear_carrera_form),
    path('director/', director_form),
    path('materia/', materia_form),
    path('carreras/', mostrar_carreras),
    path('directores/', ver_directores),
    path('materias/', ver_materias),
    path('buscar/', buscar_comision),
    path('ver/', buscar_director),
    path('mostrar/', buscar_materia),
    path('show/', show_html),
    path('carrera/<int:pk>', DetalleCarrera.as_view(), name="CarreraDetail"),
]

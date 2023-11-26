from django.urls import path
from MiApp.views import crear_carrera, show_html, mostrar_carreras, crear_carrera_form, buscar_comision

urlpatterns = [
    path('crear/', crear_carrera),
    path('carrera/', crear_carrera_form),
    path('show/', show_html),
    path('carreras/', mostrar_carreras),
    path('buscar/', buscar_comision),
]

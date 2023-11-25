from django.urls import path
from MiApp.views import crear_carrera, show_html, mostrar_carreras

urlpatterns = [
    path('crear/', crear_carrera),
    path('show/', show_html),
    path('carreras/', mostrar_carreras),
]

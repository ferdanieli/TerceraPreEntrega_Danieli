from django.contrib import admin
from django.urls import path, include
from MiApp.views import mostrar_carreras

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_carreras),
    path('app/', include('MiApp.urls')),
]

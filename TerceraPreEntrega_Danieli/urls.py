from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from MiApp.views import mostrar_carreras

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_carreras),
    path('app/', include('MiApp.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
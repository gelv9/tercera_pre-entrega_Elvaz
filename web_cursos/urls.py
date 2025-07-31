from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
import usuarios.urls

def inicio(request):
    return HttpResponse('Bienvenido, estas logueado.')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('', include('cursos.urls')),
    path('usuarios/', include((usuarios.urls, 'usuarios'), namespace='usuarios')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


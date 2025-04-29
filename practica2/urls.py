from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from libros.views import AutorViewSet, LibroViewSet
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Bienvenido a la API de Libros. Accede a /api/ para ver los endpoints disponibles.")

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'libros', LibroViewSet)

urlpatterns = [
    path('', welcome),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

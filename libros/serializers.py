from rest_framework import serializers
from .models import Autor, Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'fecha_nacimiento']

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'fecha_publicacion'] 
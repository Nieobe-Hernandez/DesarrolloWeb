from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Alumno
from .serializers import AlumnoSerializer

from django.shortcuts import render, redirect
from .forms import AlumnoForm


class AlumnoViewSet(viewsets.ModelViewSet):
    # esta variable me dice de donde saco el modelo y la informacion de DB
    queryset = Alumno.objects.all()
    
    # como serializar la informacion
    serializer_class = AlumnoSerializer
    
    # como renderizar mis respuestas
    renderer_classes = [JSONRenderer]
    
    #permitir filtrar que metodos HTTP se pueden usar
    #por defecto si no la delcaro se ocupan todos (get, post, put, delete)
    #http_method_names = ['get', 'post', 'put', 'delete']
    
def alumnos_view(request):
    form = AlumnoForm()
    return render(request, 'Hernandez_Jaqueline.html', {'form': form})
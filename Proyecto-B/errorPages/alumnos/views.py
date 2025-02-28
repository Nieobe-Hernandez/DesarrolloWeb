from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Alumno
from .serializers import AlumnoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    # esta variable me dice de donde saco el modelo y la información de base de datos
    queryset  = Alumno.objects.all()
    
    # como serializar la información 
    serializer_class = AlumnoSerializer
    
    # como renderizar la información(respuesta)
    renderer_classes = [JSONRenderer]
    
    #permitir filtar que metodos http se pueden usar
    #si no lo declaro funcionan todos
   # http_method_names = ['get', 'post', 'put', 'delete']
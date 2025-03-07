from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from .forms import productoForm
from django.shortcuts import render

class ProductoViewSet(viewsets.ModelViewSet):

    # esta variable me dice de donde saco el modelo y la información de base de datos
    queryset  = Producto.objects.all()
    
    # como serializar la información 
    serializer_class = ProductoSerializer
    
    # como renderizar la información(respuesta)
    renderer_classes = [JSONRenderer]
    
    #permitir filtar que metodos http se pueden usar
    #si no lo declaro funcionan todos
   # http_method_names = ['get', 'post', 'put', 'delete']
   
def agregar_view (request):
    form = productoForm()
    return render(request, 'agregar.html', {'form': form})
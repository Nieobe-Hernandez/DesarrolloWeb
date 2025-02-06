from django.shortcuts import render
from django.http import HttpResponse
from app.utils import *
from .models import Usuarios


#def index(request):

 #   return HttpResponse("<h1>Hola Mundo!</h1>")
 
def index(request):
     return render(request,'index.html',status=200)
 
def error_404_view(request,exception):
    return render(request,'404.html',status=404)


def error_500_view(request,exception):
    return render(request,'500.html',status=500)

def generar_error(request):
    return 7/0

def onepage(request):
    return render(request, 'onepage.html', status=200)

def prueba_front(request):
    texto = request.GET.get('texto', '')
    
    #Vamos a generar informacion en python
    objeto1 = {
        'id': '0001',
        'title': texto,
        'description': 'texto generico 1'
    }
    objeto2 = {
        'id': '0002',
        'title': ' titulo 2',
        'description': 'texto generico 2'
    }
    
    objeto3 = {
        'id': '0003',
        'title': ' titulo 3',
        'description': 'texto generico 3'
    }
    conjunto = [objeto1,objeto2,objeto3]
    
    #como mandar un objeto(variable python a la vista)
    
    
    #obtener los datos de la base de datos
    personas = Usuarios.objects.values('id','nombres','apellidos', 'edad')
    listaPersonas = list(personas)
    
    return render(
        request,
        'prueba.html',
        {'objeto': objeto1, 'arreglo': conjunto, 'lista': listaPersonas}
    )
    
def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

from django.http import JsonResponse
from django.shortcuts import render
from .models import ErrorLog

def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})
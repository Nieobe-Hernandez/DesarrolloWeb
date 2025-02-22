from django.shortcuts import get_object_or_404, render, redirect
from .models import Categoria
from django.http import JsonResponse
from .forms import categoriaForm

#Vista que devuelve las categorias como JSON
def lista_categorias(request):
    #Obtener todos los objetos de categorias de la base de datos
    categorias = Categoria.objects.all()
    #Vamos a guardar los datos en un dict
    #este diccionario fue creado al aire y no es seguro
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias 
    ]
    return JsonResponse(data, safe=False)

def ver_categorias(request):
    return render(request, 'ver_categorias.html', status=200)

def agregar_categoria(request):
    #checar si vengo del form
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('json')
    else:
        form = categoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})


#Función que agrega un producto con un objeto JSON

import json
def registrar_categoria(request):
    #Checar si nuestra request es de tipo POST
    if request.method == 'POST':
        #Quiere decir que si estoy manejando el request
        try:
            data = json.loads(request.body) #Parametro es un texto que deberia ser un JSON
            categoria = Categoria.objects.create(
                nombre=data['nombre'],
                imagen=data['imagen']
            ) #Create directamente mete el objeto en la bd
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoso',
                    'id': categoria.id
                }, status=201
            )
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {'error': str(e)}, status = 400
            )
    #Si no es POST el request    
    return JsonResponse(
        {'error':'El método no está soportado'}, status=405
    )

#Funciones para el método PUT
def actualizar_categoria(request,id_categoria):
    if request.method == 'PUT':
        categoria = get_object_or_404(Categoria, id=id_categoria)
        try:
            #La información de la modificación del producto viene del body del request
            data = json.loads(request.body)
            categoria.nombre = data.get('nombre', categoria.nombre)
            categoria.imagen = data.get('imagen', categoria.imagen)
            categoria.save()
            return JsonResponse({'mensaje': 'Categoria actualizada correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse(
        {'error':'El método no es PUT'}, status=405
    )

#Funciones para DELETE
def borrar_categoria(request, id_categoria):
    if request.method == 'DELETE':
        categoria = get_object_or_404(Categoria, id=id_categoria)
        categoria.delete() #<-- borra fisicamente el registro de la BD
        return JsonResponse({'mensaje': 'Categoria eliminada correctamente'}, status=200)
    return JsonResponse(
        {'error':'El método no es DELETE'}, status=405
    )

#Función adicional para GET de retornar una categoria especifica
def obtener_categoria(request, id_categoria):
    if request.method == 'GET':
        categoria = get_object_or_404(Categoria, id=id_categoria)
        data = {
            "id": categoria.id,
            "nombre": categoria.nombre,
            "imagen": categoria.imagen
        }
        return JsonResponse(data, status=200)
    return JsonResponse(
        {'error':'El método no es GET'}, status=405
    )
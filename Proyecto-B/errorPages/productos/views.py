from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.http import JsonResponse
from .forms import productoForm

#Vista que devuelve los Productos como JSON
def lista_productos(request):
    #Obtener todos los objetos de productos de la base de datos
    productos = Producto.objects.all()
    #Vamos a guardar los datos en un dict
    #este diccionario fue creado al aire y no es seguro
    data = [
        {
            'id': p.id,
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos 
    ]
    return JsonResponse(data, safe=False)

def ver_productos(request):
    return render(request, 'ver.html', status=200)

def agregar_producto(request):
    #checar si vengo del form
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = productoForm()
    return render(request, 'agregar.html', {'form': form})

import json
#vista que devuelve los productos en formato JSON
def registrar_producto(request):
    #checar si vengo del form y si es un POST
    if request.method == 'POST':
        #quiere decir que estoy manejando el request
        try:
            data = json.loads(request.body) #parsear el JSON
            producto = Producto.objects.create(
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            ) #crear el objeto en la base de datos
            return JsonResponse(
                {
                    'mensaje': 'Producto creado',
                    'id': producto.id
                    }, status=201
                )
        except Exception as e:
            return JsonResponse(
                {
                    'error': str(e)
                }, status=400
            )
    #si no es un POST, devolver un error
    return JsonResponse(
        {
            'error': 'Metodo no permitido'
        }, status=405
    )
    
    #funciones para el metodo PUT 
def actualizar_producto (request,id_producto):
        #checar si vengo del form y si es un POST
        if request.method == 'PUT':
            producto = get_object_or_404(Producto, id=id_producto)
            try:
                #la informacion de la modificacion del producto viene del body del request
                data = json.loads(request.body)
                producto.nombre = data.get('nombre', producto.nombre)
                producto.precio = data.get('precio', producto.precio)
                producto.imagen = data.get('imagen', producto.imagen)
                producto.save()
                return JsonResponse(
                    {
                        'mensaje': 'Producto actualizado correctamente'
                    }, status=200
                )
            except Exception as e:
                return JsonResponse(
                    {
                        'error': str(e)
                    }, status=400
                )
        #si no es un PUT, devolver un error
        return JsonResponse(
            {
                'error': 'Metodo no permitido'
            }, status=405
        )
           
    #funciones para el metodo DELETE
def borrar_producto(request,id_producto):
        if request.method == 'DELETE':
            producto = get_object_or_404(Producto, id=id_producto)
            producto.delete() # borra fisicamente el objeto de la base de datos
            return JsonResponse(
                {
                    'mensaje': 'Producto eliminado correctamente'
                }, status=200
            )
        #si no es un DELETE, devolver un error
        return JsonResponse(
            {
                'error': 'Metodo no permitido'
            }, status=405
        )
    
    #funciones para el metodo GET (obtener un solo producto)
def obtener_producto(request,id_producto):
        if request.method == 'GET':
            producto = get_object_or_404(Producto, id=id_producto)
            data = { #creamos un diccionario con los datos del producto
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'imagen': producto.imagen
            }
            return JsonResponse(
                data , status=200
            )
        #si no es un GET, devolver un error
        return JsonResponse(
            {
                'error': 'Metodo no permitido'
            }, status=405
        )
    
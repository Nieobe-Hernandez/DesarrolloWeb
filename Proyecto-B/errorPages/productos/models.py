from django.db import models
from categorías.models import Categoria
class DetallesProducto(models.Model):
    #Atributos de clase
    descripcion = models.CharField(max_length=300)
    fecha_caducidad = models.DateField()
    
class Proveedor(models.Model):
    #Atributos de clase
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    
#clase de productos
class Producto(models.Model):
    #Atributos de clase
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.URLField()
    #primer parametro es el modelo con el que se relaciona y el segundo es la acción que se realiza
    detalles_producto = models.OneToOneField(DetallesProducto, on_delete=models.CASCADE, null=True, blank=True)
    #cuando se rquiera usar una relación se usa un campo:
    # OneToOneField (1:1)
    # ForeignKey (1:N)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    # ManyToManyFieldn(M:M)
    proveedor = models.ManyToManyField(Proveedor)
    
    def __str__(self):
        return self.nombre
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen
        }
        


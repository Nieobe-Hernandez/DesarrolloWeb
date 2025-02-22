from django.db import models

#clase de productos
class Producto(models.Model):
    #Atributos de clase
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.URLField()
    
    def __str__(self):
        return self.nombre
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen
        }
from django.db import models

#Clase de categoria
class Categoria(models.Model):
    #Atributos de clase
    nombre = models.CharField(max_length=50)
    imagen = models.URLField()
    
    def __str__(self):
        return self.nombre
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'imagen': self.imagen
        }
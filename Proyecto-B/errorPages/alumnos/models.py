from django.db import models

#clase de alumnos
class Alumno(models.Model):
    #Atributos de clase
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    edad = models.DecimalField(max_digits=2, decimal_places=0)
    matricula = models.CharField(max_length=11, unique=True)
    correo = models.EmailField(max_length=254, unique=True)
    
    def __str__(self):
        return self.nombre
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'matricula': self.matricula,
            'correo': self.correo
        }
from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nombre': 'Nombre del alumno',
            'apellido': 'Apellido del alumno',
            'edad': 'Edad del alumno',
            'matricula': 'Matrícula del alumno',
            'correo': 'Correo del alumno'
        }

        error_messages = {
            'nombre': {'required': 'El alumno debe tener un nombre'},
            'apellido': {'required': 'El alumno debe tener un apellido'},
            'edad': {'required': 'El alumno debe tener una edad'},
            'matricula': {'required': 'El alumno debe tener una matrícula'},
            'correo': {'required': 'El alumno debe tener un correo'}
        }
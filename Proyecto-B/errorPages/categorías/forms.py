#Generar aqui todos los formularios HTML que vamos a ocupar
from django import forms
from .models import Categoria

#Crear una clase para cada formulario que necesitemos
class categoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        #Que campos van a verse en el form
        fields = ['nombre', 'imagen']

        #Personalizar mis inputs
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aqui el nombre de la categoria',
                    'required': True
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aqui la imagen de la categoria',
                    'required': True
                }
            ),
        }

        #Etiquetas
        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la imagen'
        }

        #Personalizar los mensajes de error
        error_messages = {
            'imagen': {
                'required': 'La categoria debe tener una imagen',
                'invalid': 'Ingresa un URL valido'
            }, 
            'nombre': {
                'required': 'La categoria debe tener un nombre',
            }
        }
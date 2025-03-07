#Generar aqui todos los formularios HTML que vamos a ocupar
from django import forms
from .models import Producto

#Crear una clase para cada formulario que necesitemos
class productoForm(forms.ModelForm):

    class Meta:
        model = Producto
        #Que campos van a verse en el form
        fields = ['nombre', 'precio', 'imagen']

        #Personalizar mis inputs
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aqui el nombre del producto',
                    'required': True
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aqui el precio del producto',
                    'required': True
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aqui la imagen del producto',
                    'required': True
                }
            ),
        }

        #Etiquetas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen'
        }

        #Personalizar los mensajes de error
        error_messages = {
            'precio': {
                'required': 'El precio no puede estar vacio',
                'invalid': 'Ingresa un precio valido'
            }
        }
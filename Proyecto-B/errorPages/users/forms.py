from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Primer formulario: Registro de usuario
class CustomUserCreationForm(UserCreationForm):
    
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'pattern': '(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&#])([A-Za-z\d$@$!%*?&#]|[^ ]){8,}$',
                'placeholder': 'Ingresa tu contraseña',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, un número y un símbolo (!, #, $, %, & o ?)',
                'required': True
            }
        )
    )
    
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'pattern': '(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&#])([A-Za-z\d$@$!%*?&#]|[^ ]){8,}$',
                'placeholder': 'Confirma tu contraseña',
                'title': 'Las contraseñas deben coincidir',
                'required': True
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Ingresa un correo con dominio @utez.edu.mx'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[a-zA-Z ]+$',
                    'title': 'Ingresa tu nombre completo'
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^\d{5}[a-zA-Z]{2}\d{3}$',
                    'title': 'La matrícula debe conincidir con el formato solicitado',
                    'maxlength': '20'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'pattern': '^\d{2}$',
                    'required': True,
                    'title': 'Ingresa tu edad en numeros',
                    'min': 1,
                    'max': 100
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'pattern': '^\d{10}$',
                    'required': True,
                    'title': 'Ingresa tu número de teléfono a 10 digitos',
                    'maxlength': '10'
                }
            )
        }

# Segundo formulario: Inicio de sesión
class CustomUserLoginForm(AuthenticationForm):
    pass
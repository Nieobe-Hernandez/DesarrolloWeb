from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import re
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "required": True,
                "placeholder": "Contraseña",
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "required": True,
                "placeholder": "Confirmar contraseña",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "name",
            "surname",
            "control_number",
            "age",
            "tel",
            "address",
            "password1",
            "password2",
        ]

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Correo electrónico",
                    "title": "Correo electrónico de la UTEZ",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Nombre:",
                    "title": "Nombre(s)",
                }
            ),
            "surname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Apellido:",
                    "title": "Apellido paterno y materno",
                }
            ),
            "control_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Número de control:",
                    "title": "Número de control de 9 dígitos",
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Edad:",

                    "title": "Edad en años",
                }
            ),
            "tel": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Teléfono:",
                    "title": "10 dígitos",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Dirección:",
                    "title": "Dirección completa",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$", email):
            raise forms.ValidationError("El correo debe ser del dominio @utez.edu.mx")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if not re.match(
            r"^(?=.*\d)(?=.*[!#$%&?])(?=.*[A-Z])(?=.*[a-z]).{8,}$", password1
        ):
            raise forms.ValidationError(
                "La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial (!, #, $, %, & o ?)."
            )
        return password1

    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        if not re.match(r"^\d{5}[a-zA-Z]{2}\d{3}$", control_number):
            raise forms.ValidationError(
                "El número de control debe tener exactamente 10 caracteres con el formato correcto."
            )
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        if not re.match(r"^\d{10}$", str(tel)):
            raise forms.ValidationError(
                "El teléfono debe contener exactamente 10 dígitos."
            )
        return tel

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 1 or age > 120:
            raise forms.ValidationError("La edad debe estar entre 1 y 120 años.")
        return age

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 2 or len(name) > 100:
            raise forms.ValidationError(
                "El nombre debe tener entre 2 y 100 caracteres."
            )
        return name

    def clean_surname(self):
        surname = self.cleaned_data.get("surname")
        if len(surname) < 2 or len(surname) > 100:
            raise forms.ValidationError(
                "El apellido debe tener entre 2 y 100 caracteres."
            )
        return surname

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data


class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "required": True,
                "pattern": "^[a-zA-Z0-9]+@utez\.edu\.mx$",
                "placeholder": "Correo electrónico",
                "title": "Correo electrónico de la UTEZ",
            }
        )
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "required": True,
                "placeholder": "Contraseña",
                "pattern": "^(?=.*\d)(?=.*[!#$%&?])(?=.*[A-Z])(?=.*[a-z]).{8,}$",
                "title": "Debe contener al menos 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial",
            }
        ),
    )

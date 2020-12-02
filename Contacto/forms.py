from django import forms

class FormularioContacto(forms.Form):
    Nombre = forms.CharField(label='Nombre', required=True, max_length=30)
    Apellidos = forms.CharField(label='Apellidos', required=True, max_length=60)
    Email = forms.CharField(label='Correo Electronico', required=True, max_length=100)
    Contenido= forms.CharField(label='Contenido')

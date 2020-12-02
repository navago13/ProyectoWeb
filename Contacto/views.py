from django.shortcuts import render
from .forms import FormularioContacto

# Create your views here.

def MiContacto(request):

    Formulario=FormularioContacto()

    return render(request,"Contacto/Contacto.html",{"Formulario":Formulario})

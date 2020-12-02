from django.shortcuts import render, HttpResponse


from Servicios.models import Servicios

# Create your views here.

def Inicio(request):

    return render(request,"ProyectoWebApp/Inicio.html")

 

def Tienda(request):

    return render(request,"ProyectoWebApp/Tienda.html")

 

 


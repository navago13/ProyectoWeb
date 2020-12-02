from django.shortcuts import render

from Servicios.models import Servicios

# Create your views here.

def MiServicios(request):

    Variable = Servicios.objects.all()

    return render(request,"Servicios/Servicios.html", {"Variable": Variable})

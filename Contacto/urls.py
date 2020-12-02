from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.MiContacto, name='MiContacto'), 
]
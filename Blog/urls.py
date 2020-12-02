from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.MiBlog, name='MiBlog'),
    path('categoria/<int:categoria_id>/', views.Micategoria, name='Micategoria'),
]
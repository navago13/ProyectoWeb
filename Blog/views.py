from django.shortcuts import render
from Blog.models import Post,Categoria

# Create your views here.

def MiBlog(request):

    posts=Post.objects.all()

    return render(request,"Blog/Blog.html",{'posts': posts})


def Micategoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)

    return render(request, "Blog/Categorias.html", {'categoria':categoria, 'posts': posts})
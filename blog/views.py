from django.shortcuts import render
from .models import Proyecto, EntradaBlog, SobreMi, Certificado

def index(request):
    return render(request, 'blog/index.html')

def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'blog/proyectos.html', {'proyectos': proyectos})

def blog_view(request):
    entradas = EntradaBlog.objects.all()
    return render(request, 'blog/blog.html', {'entradas': entradas})

def sobre_mi(request):
    datos = SobreMi.objects.first()
    return render(request, 'blog/sobre_mi.html', {'datos': datos})

def certificados(request):
    certificados = Certificado.objects.all()
    return render(request, 'blog/certificados.html', {'certificados': certificados})


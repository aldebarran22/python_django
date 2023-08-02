from django.shortcuts import render

# Create your views here.

from aplicacion6.models import Author, Book
from django.db.models import Sum

def index(request):
    # mostrar la página principal con unos enlaces:
    return render(request, 'index.html')

def autores(request):
    # Accedemos al modelo: Recuento de autores:
    numAutores = Author.objects.count()

    # Precio total de los libros:
    d = Book.objects.aggregate(precio_total=Sum('price'))  
    #print(d) 

    # Recuperar todos los libros:
    libros = Book.objects.all().order_by("-price")

    #print(type(libros[0].authors))

    # Cargamos la información en el contexto y pasamos el contexto al template
    contexto = {"numAutores":numAutores, "totalLibros":d, "libros":libros}
    return render(request, 'autores.html', context=contexto)

def calculadora(request):
    return render(request, 'calculadora.html')

def infoRequest(request):
    contexto = {"meta": request.META}
    return render(request, 'info_request.html', context=contexto)
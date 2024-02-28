from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from datetime import datetime
from tutorial.models import Book


def index(request):
    # Mostrar en el index la cantidad de libros y editorial que
    # tiene la biblioteca.
    horaActual = datetime.now()
    hora = horaActual.strftime("%d/%m/%Y %H:%M:%S")
    numLibros = Book.objects.count()
    # Enlaces de interes:
    enlaces = {
        "El país": "http://www.elpais.com",
        "El mundo": "http://www.elmundo.com",
        "Marca": "http://www.elpais.com",
    }
    contexto = {"ahora": hora, "numLibros": numLibros, "enlaces": enlaces}
    return render(request, "index.html", contexto)


def libros(request):
    L = Book.objects.all()
    numLibros = len(L)
    return render(request, "libros.html", {"libros": L, "numLibros": numLibros})

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum

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
        "El país": "https://elpais.com",
        "El mundo": "http://www.elmundo.com",
        "Marca": "http://www.marca.com",
    }
    contexto = {"ahora": hora, "numLibros": numLibros, "enlaces": enlaces}
    return render(request, "index.html", contexto)


def libros(request):
    L = Book.objects.all()
    numLibros = len(L)
    suma = Book.objects.all().aggregate(Sum("price"))["price__sum"]
    return render(
        request, "libros.html", {"suma": suma, "libros": L, "numLibros": numLibros}
    )

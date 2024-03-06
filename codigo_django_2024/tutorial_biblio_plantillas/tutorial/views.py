from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
from datetime import datetime
from tutorial.models import Book, Fotografia


def getEnlaces():
    # Enlaces de interes:
    enlaces = {
        "El país": "https://elpais.com",
        "El mundo": "http://www.elmundo.com",
        "Marca": "http://www.marca.com",
    }
    return enlaces


def index(request):
    # Mostrar en el index la cantidad de libros y editorial que
    # tiene la biblioteca.
    horaActual = datetime.now()
    hora = horaActual.strftime("%d/%m/%Y %H:%M:%S")
    numLibros = Book.objects.count()
    contexto = {"ahora": hora, "numLibros": numLibros, "enlaces": getEnlaces()}
    return render(request, "index.html", contexto)


def libros(request):
    L = Book.objects.all()
    numLibros = len(L)
    suma = Book.objects.all().aggregate(Sum("price"))["price__sum"]
    return render(
        request,
        "libros.html",
        {"suma": suma, "libros": L, "numLibros": numLibros, "enlaces": getEnlaces()},
    )


def galeria(request):
    fotos = Fotografia.objects.all()
    contexto = {"enlaces": getEnlaces(), "fotos": fotos}
    return render(request, "galeria.html", contexto)


def info_request(request):
    contexto = {"meta": request.META, "enlaces": getEnlaces()}
    return render(request, "info.html", contexto)


def formulario(request):
    return render(request, "formulario.html", {"enlaces": getEnlaces()})

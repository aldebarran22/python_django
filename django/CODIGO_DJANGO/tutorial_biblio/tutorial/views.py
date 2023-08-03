from django.shortcuts import render
from django.http import HttpResponse

from tutorial.models import Fotografia
from tutorial.models import Book

import csv

# Create your views here.
def index(request):
    return render(request, 'index.html')

def galeria(request):
    fotos = Fotografia.objects.all()
    contexto = {"fotos":fotos}
    return render(request, 'galeria.html', context=contexto)

def librosxml(request):
    L = Book.objects.all()
    contexto = {"libros": L}
    return render(request, 'libros.xml', \
                  context=contexto, content_type='text/xml')

def libroscsv(request):
    L = Book.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=libros.csv'
    writer = csv.writer(response)
    cabeceras = Book.getCabeceras()
    writer.writerow(cabeceras)
    for libro in L:
        fila = libro.tolist()
        writer.writerow(fila)
    return response



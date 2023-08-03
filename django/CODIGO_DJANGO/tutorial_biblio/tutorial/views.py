from django.shortcuts import render
from tutorial.models import Fotografia
from tutorial.models import Book

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

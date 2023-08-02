from django.shortcuts import render

# Create your views here.

from aplicacion6.models import Author

def index(request):
    # mostrar la página principal con unos enlaces:
    return render(request, 'index.html')

def autores(request):
    # Accedemos al modelo:
    numAutores = Author.objects.count()

    # Cargamos la información en el contexto y pasamos el contexto al template
    contexto = {"numAutores":numAutores}
    return render(request, 'autores.html', context=contexto)


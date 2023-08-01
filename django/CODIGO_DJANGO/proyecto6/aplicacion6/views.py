from django.shortcuts import render

# Create your views here.

from aplicacion6.models import Author

def index(request):
    # Accedemos al modelo:
    numAutores = Author.objects.count()

    # Cargamos la información en el contexto y pasamos el contexto al template
    contexto = {"numAutores":numAutores}
    return render(request, 'index.html', contexto)

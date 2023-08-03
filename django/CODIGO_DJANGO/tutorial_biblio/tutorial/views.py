from django.shortcuts import render
from tutorial.models import Fotografia

# Create your views here.
def index(request):
    return render(request, 'index.html')

def galeria(request):
    fotos = Fotografia.objects.all()
    contexto = {"fotos":fotos}
    return render(request, 'galeria.html', context=contexto)
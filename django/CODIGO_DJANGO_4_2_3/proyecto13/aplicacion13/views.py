from django.shortcuts import render

# Create your views here.
from aplicacion13.models import Fotografia


def index(request):
    return render(request, "index.html")


def galeria(request):
    fotos = Fotografia.objects.all()
    contexto = {"fotos":fotos}
    return render(request, "galeria.html", contexto)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from datetime import datetime


def index(request):
    horaActual = datetime.now()
    ahora = horaActual.strftime("%d/%m/%Y %H:%M:%S")
    contexto = {"ahora": ahora}
    return render(request, "index.html", contexto)



def saludar(request):
    print("Ha solicitado saludar")
    return HttpResponse("<h3>Página de saludo</h3>")


def buscarLibro(request, id):
    print("id:", id)
    return HttpResponse(f"<h3>el id es: {id}</h3>")

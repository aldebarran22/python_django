from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from aplicacion6.models import Author, Book
from aplicacion6.forms import FormContacto
from django.db.models import Sum

def index(request):
    # mostrar la página principal con unos enlaces:
    return render(request, 'index.html')

def autores(request):
    # Accedemos al modelo: Recuento de autores:
    numAutores = Author.objects.count()

    # Precio total de los libros:
    d = Book.objects.aggregate(precio_total=Sum('price'))  
    #print(d) 

    # Recuperar todos los libros:
    libros = Book.objects.all().order_by("-price")

    #print(type(libros[0].authors))

    # Cargamos la información en el contexto y pasamos el contexto al template
    contexto = {"numAutores":numAutores, "totalLibros":d, "libros":libros}
    return render(request, 'autores.html', context=contexto)

def calculadora(request):
    return render(request, 'calculadora.html')

def infoRequest(request):
    contexto = {"meta": request.META}
    return render(request, 'info_request.html', context=contexto)

def resultados(request):

    if request.POST['numero1'].isnumeric():
        numero1 = int(request.POST['numero1'])
        print('numero1: ', numero1)

    if request.POST['numero2'].isnumeric():
        numero2 = int(request.POST['numero2'])
        print('numero2: ', numero2)

    if request.POST['operacion'] == '' or request.POST['operacion'] == 'suma':
        return HttpResponse(f'suma:  {numero1 + numero2}')

    elif request.POST['operacion'] == 'resta':
        return HttpResponse(f'resta: {numero1 - numero2}')
    

def contacto(request):
    """
    En la primera petición mostramos el formulario vacio
    Recibimos la petición GET
    Cuando envíamos el formulario lo recibimos por POST
    """
    if request.method == 'POST':
        # Ha enviado el formulario
        form = FormContacto(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            return HttpResponse(str(datos))

    else:
        # Es la primera vez, se muestra el formulario:
        form = FormContacto()

    return render(request, 'contacto.html', context={'form':form})
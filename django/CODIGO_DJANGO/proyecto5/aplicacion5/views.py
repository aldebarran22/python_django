from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(request):
    # La url sera: http://localhost:8000/hello/
    return HttpResponse("<h3>Hello World!</h3>")

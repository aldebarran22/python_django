"""
Vistas basadas en clases
"""

from tutorial.models import Book
from django.views.generic import ListView, DetailView

class ListadoLibros(ListView):
    model = Book

class DetalleLibro(DetailView):
    model = Book
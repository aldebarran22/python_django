"""
Vistas basadas en clases
"""

from tutorial.models import Book
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


class ListadoLibros(ListView):
    model = Book


class DetalleLibro(DetailView):
    model = Book


class BookDelete(DeleteView):
    model = Book
    fields = ["isbn", "name"]
    success_url = reverse_lazy("libros2")


class BookUpdate(UpdateView):
    model = Book
    fields = ["isbn", "name", "price", "publisher", "authors"]


class BookCreate(CreateView):
    model = Book
    fields = ["isbn", "name", "price", "publisher", "authors"]

from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

from aplicacion11.models import Book, Author, Publisher
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ListaLibros(ListView):
    model = Book

class DetalleLibro(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['isbn','name','price','publisher','authors']

class BookUpdate(UpdateView):
    model = Book
    fields = ['isbn','name','price','publisher','authors']    

class BookDelete(DeleteView):
    model = Book
    fields = ['isbn','name','price','publisher','authors']    
    success_url = reverse_lazy('listalibros')
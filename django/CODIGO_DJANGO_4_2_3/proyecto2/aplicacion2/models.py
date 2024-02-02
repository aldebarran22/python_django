from django.db import models

# Create your models here.

"""
Autor (nombre, apellidos, correo …), 
Editor (nombre, domicilio, ciudad, provincia, país, web). 
Y los libros: donde un libro tiene un solo autor y un solo editor
"""

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)

class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    web = models.URLField(max_length=80)

class Libro(models.Model):
    isbn = models.CharField(max_length=25, null=True)
    titulo = models.CharField(max_length=30)
    precio = models.FloatField()    
    
    # Claves Foraneas:
    # Este es el caso que el libro solo tiene un autor
    #autor = models.ForeignKey(Autor, on_delete=models.PROTECT)    
    editor = models.ForeignKey(Editor, on_delete=models.PROTECT)

    # Si el libro puede tener varios autores tenemos una rel: many to many
    autores = models.ManyToManyField(Autor)




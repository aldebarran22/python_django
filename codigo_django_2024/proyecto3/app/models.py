from django.db import models

"""
PROCESO REALIZADO:
1) Borro la migración 0004 que añadía la tabla LibrosAutores 
con el campo páginas.
2) Borro la migración 0005 que borraba la tabla generada por django.
3) Volvemos a crear la migración 0004 para borrar la tabla.
LibroAutores y el campo autores de los libros.
4) Comprobar en la BD que se borra la tabla.
5) Volvemos a descomentar la clase LibrosAutores y el campo autores 
de Libros generar migración y migrate. Migración 0005.
6) En esta ya tenemos la nueva tabla libroautores con el 
campo paginas.
"""


# Create your models here.
class Autor(models.Model):
    # Los campos del autor
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=80)


class Editor(models.Model):
    # Los campos del editor
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30)  ###
    ciudad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    web = models.URLField(max_length=50)
    correo = models.EmailField(max_length=80, blank=True)


class LibroAutores(models.Model):
    libro = models.ForeignKey("Libro", on_delete=models.PROTECT)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    paginas = models.IntegerField(blank=True, null=True)


class Libro(models.Model):
    # Los campos del libro
    isbn = models.CharField(max_length=20)
    titulo = models.CharField(max_length=30)
    precio = models.FloatField()
    descuento = models.FloatField(blank=True, null=True)

    # Relaciones:
    # 1 Editor -> N Libros (de 1 a N)
    editor = models.ForeignKey(Editor, on_delete=models.PROTECT)

    # N Autores <-> M Libros (de muchos a muchos)
    autores = models.ManyToManyField(Autor, through=LibroAutores)

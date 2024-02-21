from django.db import models


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


"""
class LibroAutores(models.Model):
    libro = models.ForeignKey("Libro", on_delete=models.PROTECT)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    paginas = models.IntegerField(blank=True, null=True)
"""

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
    #autores = models.ManyToManyField(Autor, through=LibroAutores)

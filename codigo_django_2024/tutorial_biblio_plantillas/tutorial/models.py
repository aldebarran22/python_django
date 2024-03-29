from django.db import models

# Create your models here.


class Author(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Autores"


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Editores"


class Book(models.Model):
    isbn = models.CharField(max_length=9)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateField(blank=True, null=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)

    def __str__(self):
        return self.name + " precio: " + str(self.price)

    @staticmethod
    def getCabeceras():
        return ["ISBN", "NAME", "PRICE", "DATE", "PUBLISHER"]

    def toList(self):
        return [
            self.isbn,
            self.name,
            self.price,
            self.fecha_publicacion,
            self.publisher.name,
        ]

    class Meta:
        ordering = ["price"]
        verbose_name_plural = "Libros"


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)


class Fotografia(models.Model):
    titulo = models.CharField(max_length=30)
    fotografia = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.titulo

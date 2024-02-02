from django.db import models

# Create your models here.

class Lugar(models.Model):
    lugar = models.CharField(max_length=30)

    def __str__(self):
        return self.lugar

class VideoBook(models.Model):
    titulo = models.CharField(max_length=30)
    fecha = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True)
    lugar = models.ForeignKey(Lugar, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

class Fotografia(models.Model):
    titulo = models.CharField(max_length=30, null=True)
    foto = models.ImageField(upload_to="images/")
    videobook = models.ForeignKey(VideoBook, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.titulo

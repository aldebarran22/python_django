from django.db import models

# Create your models here.

class Persona(models.Model):
    objects = models.Manager()
    nombre = models.CharField(max_length=30)
    apellido1 = models.CharField(max_length=30)
    apellido2 = models.CharField(max_length=30)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()

    def to_list(self):
        return [self.nombre, self.apellido1, self.apellido2, self.dni, self.telefono, self.email]
   
    @staticmethod
    def getCabeceras():
        return ['NOMBRE','APELLIDO1','APELLIDO2','DNI','TELEFONO','EMAIL']

    def __str__(self):
        return self.nombre + " " + self.apellido1 + " " + self.apellido2
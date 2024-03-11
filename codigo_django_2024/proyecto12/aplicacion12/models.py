from django.db import models

# Create your models here.

class Cancion(models.Model):
    '''
    Esta es una clase del modelo. Representa una cancion
    '''
    titulo=models.CharField(max_length=25)
    grupo=models.CharField(max_length=30)

    class Meta:
        '''
        Utilizamos la clase Meta para añadir permisos al modelo.
        '''
        permissions=(('escuchar_cancion','escuchar cancion'), \
        ('bajar_cancion','bajar cancion'))
         

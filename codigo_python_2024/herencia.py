"""
POO en Python. Herencia simple
"""

# Opción 1)
import objetos


class Empleado2(objetos.Persona):
    pass


# Opción 2)
# from modulo import clase
from objetos import Persona


class Empleado(Persona):
    
    def __init__(self,nombre="", peso=0, altura=0.0, empresa="",sueldo=0.0):
        # Llamar al constructor de la clase Padre:
        Persona.__init__(self,nombre, peso, altura)

        # Definir los atributos de la clase Empleado:
        self.empresa = empresa
        self.sueldo = sueldo


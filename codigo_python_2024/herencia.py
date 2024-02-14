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
    pass

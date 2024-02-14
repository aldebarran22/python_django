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

    def __str__(self):
        return Persona.__str__(self)+ " "+self.empresa+" "+str(self.sueldo)


if __name__ == '__main__':
    emp = Empleado("Sara", 34, 1.8, "CAS", 2000.0)
    print(emp.__dict__)
    del(emp.__dict__['peso'])
    emp.__dict__['tno'] = 696558877
    emp.correr()
    print(emp.__dict__)
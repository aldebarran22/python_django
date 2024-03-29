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

    def __init__(self, nombre="", peso=0, altura=0.0, empresa="", sueldo=0.0):
        # Llamar al constructor de la clase Padre:
        Persona.__init__(self, nombre, peso, altura)

        # Definir los atributos de la clase Empleado:
        self.empresa = empresa
        self.sueldo = sueldo

    def __str__(self):
        return Persona.__str__(self) + " " + self.empresa + " " + str(self.sueldo)

    """
    def __lt__(self, other):
        return self.sueldo < other.sueldo
    """


class Programador(Empleado):

    def __init__(
        self, nombre="", peso=0, altura=0.0, empresa="", sueldo=0.0, lenguajes=[]
    ):
        Empleado.__init__(self, nombre, peso, altura, empresa, sueldo)
        self.lenguajes = lenguajes


def testEmpleado():
    emp = Empleado("Sara", 60, 1.8, "CAS", 2000.0)
    emp2 = Empleado("Raquel", 60, 1.79, "TRT", 2500.0)
    if emp < emp2:
        print(emp.nombre, "es menor", emp2.nombre)
    else:
        print(emp2.nombre, "es menor", emp.nombre)

    print(emp.__dict__)
    # del(emp.__dict__['peso'])
    emp.__dict__["tno"] = 696558877
    emp.correr()
    print(emp.__dict__)


def testProgramador():
    pg1 = Programador("Sara", 60, 1.8, "CAS", 2000.0, ["python", "Java"])
    pg2 = Programador("Raquel", 60, 1.79, "TRT", 2500.0, ["python", "C++"])
    if pg1 < pg2:
        print(pg1.nombre, "es menor", pg2.nombre)
    else:
        print(pg2.nombre, "es menor", pg1.nombre)


if __name__ == "__main__":
    # testEmpleado()
    testProgramador()

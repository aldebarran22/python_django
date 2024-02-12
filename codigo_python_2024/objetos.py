"""
POO en Python
"""


class Persona:
    """
    Implementación de la clase Persona
    """

    def __init__(self, nombre="", peso=0, altura=0.0):
        # Definición de atributos:
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return self.nombre + " " + str(self.peso) + " " + str(self.altura)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        if self.peso == other.peso:
            if self.altura < other.altura:
                return True
            else:
                return False
        elif self.peso < other.peso:
            return True
        else:
            return False

    def correr(self):
        print(self.nombre, "está corriendo")


if __name__ == "__main__":
    p1 = Persona("Ana", 66, 1.77)
    p2 = Persona("Miguel", 80, altura=1.8)
    p3 = Persona("Eva", 50, 1.82)
    # objeto.metodo()
    p1.correr()
    print(p1)  # print(str(p1))  print(p1.__str__())
    L = [p1, p2, p3]
    print(L)
    L.sort()
    print(L)

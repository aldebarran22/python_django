"""
POO en Python
"""

class Persona:
    """
    Implementación de la clase Persona
    """
        
    def __init__(self, nombre="", peso=0, altura=0.0):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def correr(self):
        print(self.nombre,'está corriendo')

if __name__ == '__main__':
    p1 = Persona("Ana")
    p2 = Persona("Miguel", altura=1.8)
    p3 = Persona("Eva", 34, 1.82)
    # objeto.metodo()
    p1.correr()
    print(p1)


    


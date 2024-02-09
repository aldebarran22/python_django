"""
Funciones en python
"""

def sumar(x,y):
    """
    Suma el valor de x e y.
    """
    return x+y

def sumar3(x,y,z):
    """
    Suma el valor de x, y, z.
    """
    return x+y+z

if __name__ == '__main__':
    # EL módulo está en ejecución
    print('suma de 5 y 6: ', sumar(5,6)) # forma posicional
    print('suma de 5 y 6: ', sumar(y=6, x=5)) # forma nominal
    t = (5,6)
    print('suma de 5 y 6: ', sumar(*t)) # con una tupla
    L = [5,6]
    print('suma de 5 y 6: ', sumar(*L)) # con una tupla
    d = {"x":5, "y":6}
    print('suma de 5 y 6: ', sumar(**d)) # con un diccionario
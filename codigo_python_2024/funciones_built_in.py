"""
Funciones definidas dentro de Python
"""

import math


def calcularOperaciones(coleccion):
    print("Tipo: ", type(coleccion))
    print("suma:", sum(coleccion))
    print("min:", min(coleccion))
    print("max:", max(coleccion))
    print("len:", len(coleccion))
    print("promedio:", sum(coleccion) / len(coleccion))
    print()


# Operaciones con una lista:
L = [1, 3, 4, 5, 6, 7, 8, 1]
calcularOperaciones(L)

# Operaciones con una tupla:
t = (1, 3, 4, 5, 6, 7, 8, 1)
calcularOperaciones(t)

# Operaciones con un conjunto:
c = {1, 3, 4, 5, 6, 7, 8, 1}
calcularOperaciones(c)

# Redondeos:
print(round(2.356, 2), math.floor(1.9999), math.ceil(1.0000001))

# Ordenar otras colecciones:
L2 = sorted(t)
print(t)
print(L2)

L3 = sorted(c, reverse=True)
print(c)
print(L3)
"""
List compre. con listas, diccionarios, conjuntos.
tuplas (OJO)
"""

from random import randint

# Generar una lista de números aleatorios:
L = [randint(1,30) for _ in range(20)]
print(L)

c = {randint(1,30) for _ in range(20)}
print(c, len(c))
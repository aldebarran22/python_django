"""
Ordenar colecciones en Python. Funciones lambda
"""

# Ordenar una lista de tuplas:
L = [("Sara", 24, 1.7), ("Raúl", 44, 1.79), ("Eva", 56, 1.88), ("Gema", 35, 1.78)]
L.sort()  # Por defecto ordena por el primer campo de la tupla (str)
print(L)
L.sort(key=lambda t: t[1])
print(L)

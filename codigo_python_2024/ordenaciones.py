"""
Ordenar colecciones en Python. Funciones lambda
"""


def ordenar(t):
    pass


# Ordenar una lista de tuplas:
L = [("Sara", 44, 1.9), ("Raúl", 44, 1.79), ("Eva", 56, 1.88), ("Gema", 56, 1.78)]
L.sort()  # Por defecto ordena por el primer campo de la tupla (str)
print(L)
L.sort(key=lambda t: t[1])
print(L)
# Ordenar por edad y altura
L.sort(key=lambda t: (t[1], t[2]))
print(L)
# L = [(12,30,5),(9,36,0),(12,8,34)]

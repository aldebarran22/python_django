"""
Ordenar colecciones en Python. Funciones lambda
"""


def ordenar(t):
    pass


def dateToInt(fecha):
    L = fecha.split('-')
    L[0],L[2] = L[2],L[0]
    s = "".join(L)
    return int(s)

"""
i = dateToInt("14-02-2024")
print(i)
exit()
"""

# Ordenar una lista de tuplas:
L = [("Sara", 44, 1.9), ("Raúl", 44, 1.79), ("Eva", 56, 1.88), ("Gema", 56, 1.78)]
L.sort()  # Por defecto ordena por el primer campo de la tupla (str)
print(L)
L.sort(key=lambda t: t[1])
print(L)
# Ordenar por edad y altura: lambda t: t[1:]
L.sort(key=lambda t: (t[1], t[2]), reverse=True)
print(L)
# L = [(12,30,5),(9,36,0),(12,8,34)]

L = ["14-02-2024","01-06-2022","01-07-2022","10-03-2025"]
# YYYYMMDD
L.sort(key=lambda f: dateToInt(f), reverse=True)
print(L)

L.sort(key=dateToInt)
print(L)

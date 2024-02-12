"""
Programación funcional: map, filter, reduce y list compre.
"""

from functools import reduce


def sumar(a, b):
    print(a, b)
    return a + b


def testReduce():
    L = [1, 5, 4, 6, 7, 6, 3, 2, 3, 4, 6]
    resul = reduce(sumar, L)
    print("resultado: ", resul)


def calcularIva(precio):
    return round(precio * 0.21, 2)


def test1():
    L = [120.0, 45.0, 70.0, 230.0]
    R = []
    for precio in L:
        iva = calcularIva(precio)
        R.append(iva)

    print(L)
    print(R)


def testMap():
    L = [120.0, 45.0, 70.0, 230.0]
    R = list(map(calcularIva, L))
    print(L)
    print(R)


def menores100(valor):
    if valor < 100:
        return True
    else:
        return False


def testFilter():
    # Filtrar los precios < 100:
    L = [120.0, 45.0, 70.0, 230.0, 23.04, 55, 300, 450, 1000, 21.76]
    R = list(filter(menores100, L))
    print(R)


def testListC():
    L = [120.0, 45.0, 70.0, 230.0]
    R = [calcularIva(precio) for precio in L]
    R2 = [round(precio * 0.21, 2) for precio in L]
    print(L)
    print(R)
    print(R2)


def testFilterConLC():
    # Filtrar los precios < 100:
    L = [120.0, 45.0, 70.0, 230.0, 23.04, 55, 300, 450, 1000, 21.76]
    R = [i for i in L if i < 100]
    print(R)


if __name__ == "__main__":
    # test1()
    # testMap()
    # testListC()
    # testFilter()
    # testFilterConLC()
    testReduce()

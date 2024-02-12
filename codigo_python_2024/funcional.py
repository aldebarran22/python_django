"""
Programación funcional: map, filter, reduce y list compre.
"""

from functools import reduce


def sumar(a, b):
    print(a, b)
    return a + b

def mejorCandidato(d1, d2):
    # Priorizar por los años de experiencia:
    if d1['años'] == d2["años"]:
        if d1["titulo"] == 'ing sup':
            return d1
        else:
            return d2
    elif d1['años'] > d2["años"]:
        return d1
    else:
        return d2

def testReduce():
    L = [1, 5, 4, 6, 7, 6, 3, 2, 3, 4, 6]
    print(L)
    resul = reduce(sumar, L)
    print("resultado: ", resul)

    L2 = [{"años":10, "titulo":"ing sup"}, \
          {"años":12, "titulo":"ing sup"}, \
            {"años":12, "titulo":"ing tec"}, \
                {"años":8, "titulo":"ing tec"}]
    mejor = reduce(mejorCandidato, L2)
    print(mejor)
    




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

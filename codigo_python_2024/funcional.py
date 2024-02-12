"""
Programación funcional: map, filter, reduce y list compre.
"""

def calcularIva(precio):
    return round(precio * .21, 2)

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

def testListC():
    L = [120.0, 45.0, 70.0, 230.0]
    R = [calcularIva(precio) for precio in L]
    R2 = [round(precio * 0.21, 2) for precio in L]
    print(L)
    print(R)
    print(R2)

if __name__ == '__main__':
    test1()
    testMap()
    testListC()
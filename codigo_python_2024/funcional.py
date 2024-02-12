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

if __name__ == '__main__':
    test1()
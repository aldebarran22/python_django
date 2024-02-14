"""
Ejemplo de función generadora
"""


def listaMul3(ini, fin, salto=1):
    L = []
    for i in range(ini, fin, salto):
        if i % 3 == 0:
            print("en la lista:", i)
            L.append(i)
    return L


def genMul3(ini, fin, salto=1):
    for i in range(ini, fin, salto):
        if i % 3 == 0:
            print("en el generador:", i)
            yield i


if __name__ == "__main__":
    print("LISTA:")
    for i in listaMul3(1, 10):
        print(i, end=" ")
    print()

    print("GENERADOR:")
    for i in genMul3(1, 10):
        print(i)
    print()

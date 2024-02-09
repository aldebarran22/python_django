"""
Paso de parámetros a funciones: 
- Mutable -> entran por referencia
- Inmutables -> entran por copia / valor
"""


def porCopia(numero: int) -> None:
    numero += 100


def testInmutables():
    numero = 5
    print("numero: ", numero)


def porReferencia(L: list, d: dict, c: set) -> None:
    L.append(100)
    d["nuevo"] = 1000
    c.remove(10)
    print("L", L, id(L))
    print("d: ", d, id(d))
    print("c: ", c, id(c))
    print("-" * 20)


def testMutables():
    L = [1, 2, 3, 4, 5]
    d = {"a": 1, "b": 2, "c": 3, "d": 4}
    c = {10, 20, 30, 40}
    # porReferencia(L.copy(), d.copy(), c.copy())
    porReferencia(L, d, c)
    print("L", L, id(L))
    print("d: ", d, id(d))
    print("c: ", c, id(c))


if __name__ == "__main__":
    # testMutables()
    testInmutables()

"""
Paso de parámetros a funciones: 
- Mutable -> entran por referencia
- Inmutables -> entran por copia / valor
"""


def porCopia(numero: int, cad: str, t:tuple) -> None:
    numero += 100
    cad += "adios"
    t += (4,5,6)
    print("numero: ", numero, id(numero))
    print("cad: ", cad, id(cad))
    print("t: ", t, id(t))
    print("-" * 20)


def testInmutables():
    numero = 5
    cad = "hola"
    t = (1,2,3)
    porCopia(numero, cad, t)
    print("numero: ", numero, id(numero))
    print("cad: ", cad, id(cad))
    print("t", t, id(t))


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

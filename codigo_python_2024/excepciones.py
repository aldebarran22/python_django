"""
Excepciones en Python
"""


def test1():
    # Captura una excepción e imprime el mensaje
    try:
        L = [1, 2, 3, 4, 5]
        print(L[10])
        print("fin")
    except IndexError as e:
        print(e.__class__.__name__, e)


def test2():
    # Capturar varias excepciones:
    try:
        n1 = 10
        d = {"a": 1, "b": 2, "c": 3}
        print(n1 / 10)
        print(d["z"])
    except KeyError as e:
        print(e.__class__.__name__, e)
    except ZeroDivisionError as e:
        print(e.__class__.__name__, e)


def test3():
    # Agrupar varias excepciones en una tupla:
    try:
        n1 = 10
        d = {"a": 1, "b": 2, "c": 3}
        print(n1 / 10)
        print(d["z"])
    except (KeyError, ZeroDivisionError) as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    # test1()
    # test2()
    test3()

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


if __name__ == "__main__":
    test1()

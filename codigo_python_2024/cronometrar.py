"""
Cronometra la creación de una lista con números ale.
1) con List compr
2) con un bucle for
"""

from random import randint
from datetime import datetime

n = 10000


def test1():
    t1 = datetime.now()
    L = []
    for i in range(n):
        L.append(randint(1, 1000))
    t2 = datetime.now()
    print("test1: ", t2 - t1)


def test2():
    t1 = datetime.now()
    L = [randint(1, 1000) for _ in range(n)]
    t2 = datetime.now()
    print("test2: ", t2 - t1)


if __name__ == "__main__":
    test1()
    test2()

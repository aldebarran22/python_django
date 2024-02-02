"""
Formas de llamar a una función en Python
"""

def sumar(a,b):
    return a+b

# 1 posicional:
print(sumar(1,2))

# 2 nominal
print(sumar(b=2, a=1))

# 3 con una tupla
t = (1,2)
print(sumar(t[0],t[1]))
print(sumar(*t))

# 4 con un dict:
d = {"a":1, "b":2}
print(sumar(**d))

L = [(2,4),(4,5),(1,2),(8,8),(9,9)]
L2 = []
for a,b in L:
    L2.append(sumar(a,b))
print(L2)

L3 = []
for t in L:
    L3.append(sumar(*t))
print(L3)


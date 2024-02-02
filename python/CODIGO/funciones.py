"""
Funciones en python
"""

def funcion():
    pass

def sumar(a,b):
    """
    Suma los dos parámetros que recibe
    y devuelve el valor
    """
    return a+b

def sumar3(a,b,c):
    return a+b+c

# Llamadas de forma de posicional
print("Enteros:",sumar(33,55))
print("Cadenas: ", sumar("hola","adios"))
print("listas: ", sumar([1,2,3],[4,5,6]))
print("Enteros:",sumar3(33,55,88))

# De forma nominal:
print("Enteros:",sumar(b=55, a=33))

for i in range(5):
    print(i, end="_")


# pass

"""
Paso de parámetros a una función:
Y modificar los parámetros.
inmutables: numeros, str, tuple  -> UNA COPIA
mutables: set, dict, list --> PASAN POR REFERENCIA
"""

def funcion1(L, c):
    L.append(100)
    c.add(100)

def funcion2(numero):
    numero += 100
    print('numero en funcion2: ', numero, id(numero))

L = [1,3,4,5,6,7]
c = {1,2,3,4}
print('L',L)
print('c',c)
funcion1(L,c)
print('L',L)
print('c',c)

numero = 10
funcion2(numero)
print('despues de la funcion2, numero = ', numero, id(numero))
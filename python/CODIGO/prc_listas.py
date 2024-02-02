"""
Definir una lista, pedir al usuario un número
e imprimir el número de veces que se repite el
número en la lista
Operadores: + * in y los relacionales
"""
L = [1,4,3,5,6,2,1,2,1]
n = int(input('Dime un número: '))
if n in L:
    print(f'El número se repite: {L.count(n)} veces')
else:
    print(n,'no está en la lista')

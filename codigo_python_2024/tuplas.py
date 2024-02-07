"""
Tuplas en Python
Creación, acceso a los elementos, ...
- Inicializar múltiples
- Intercambiar variables
"""
t1 = 1,2,3,4,
t2 = (5,6,7,8)
print(t1, type(t1))
print(t2, type(t2))
t3 = (4,)
print(t3, type(t3))

frase = "hola que tal"
t = tuple(frase)
print(t)
print('El espacio ocupa la pos: ', t.index(' '))
print('El 2º espacio ocupa la pos: ', t.index(' ',5))
try:
    t[0] = "X"
except Exception as e:
    print(e)

# Imprimir las posiciones que ocupan los blancos en una tupla
frase = "hola que tal el lunes"
n = frase.count(' ')
inicio = 0
for i in range(n):
    pos = frase.index(' ', inicio)
    print('pos blanco:', pos)
    inicio = pos+1


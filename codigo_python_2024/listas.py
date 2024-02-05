"""
Listas en Python. Objetos mutables
"""

# Una lista de números
L = [2,5,6,7,4,2]

# Una lista de cadenas:
nombres = ['Miguel','Ana','Sandra','Andrés']

# Acceso a los elementos:
print(L[2], L[-4])
print(L[-1], L[5])

# Slicing: listas, cadenas y tuplas
# L[ini:fin-1:salto=1]
print(L)
print('los tres primeros: ', L[0:3], L[:3])
print('los 3 últimos: ', L[-3:])
print('quitar el primero y el último:', L[1:-1])

# Bucle FOR, in, +, *
for i in nombres:
    print(i)

for pos, i in enumerate(nombres):
    print(pos, i)

nombre = "Ana"
if nombre in nombres:
    print(nombre,'esta en la lista')
    print('Está en la pos: ', nombres.index(nombre))
else:
    print('No se encuentra')

# Concatenar listas:
L1 = [1,2,3]
L2 = [40,50,60]
print(L1 + L2)

print(L1 * 4)
print('-'*50)
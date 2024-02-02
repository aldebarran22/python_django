"""
Listas en python: definición, acceso, recorridos..
"""
L = [1,4,3,5,6,2,1,2,1]
print(L, type(L))
print([1,2,3]*5)
print([1,2,3]+[4,5,6])

# Acceso a los elementos:
print('El primero',L[0])
L[0] = 1000
print(L)

for i in L:
    print(i)

for i in [1,2,3]:
    print(i)

L = [1,4,3,5,6,2,1,2,1]
print('El 1 se repite ', L.count(1))

# Slicing e índices negativos:
L = [1,2,3,4,5,6,7,8]
print('el primero: ', L[0], L[-8])
print('El ultimo: ', L[7], L[-1])

fichero = "c:/mis documentos/pdfs/cv.pdf"
L2 = fichero.split("/")
print(L2)
nombre_fichero = L2[-1]
print(nombre_fichero)

nombre = "Ana Sanz Sanchez"
L3 = nombre.split(" ")
print('el nombre: ', L3[0])

# Slicing L[ini:fin-1:salto]
# L = [1,2,3,4,5,6,7,8]
print(L)
print('los tres primeros: ', L[0:3])
print('los tres primeros: ', L[:3])
print('los tres ultimos: ', L[-3:])
print('del 3 al -3:', L[3:-3])
print('Toda la lista de dos en dos: ', L[::2])

# range(ini, fin-1, salto)
for i in range(10):
    print(i, end=' ')
print()

# Añadir elementos a una lista:
L.append(10)
print(L)

# Añadir 5 números por teclado a una lista:
L = [] # L = list()
for i in range(5):
    numero = int(input("Inserte un número entero por favor: "))
    L.append(numero)
print(L)

s = "hola que tal"
L2 = list(s)
print(L2)


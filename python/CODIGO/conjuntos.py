"""
Pruebas con conjuntos en Python:
crear, recorrer, operadores
"""

c1 = {4,5,5,5,4,3,3,2,1,8,9,0}
print(c1, type(c1))

L = [4,3,2,2,1,1,1,2,2,3,4,5,5,6,7,8]
c2 = set(L)
print(c2, type(c2))
L2 = list(set(L))
print(L2)

frase = "hola que tal"
c3 = set(frase)
print(c3)

comida = {"Juan","Pedro","Julia","Cristina"}
cena = {"Juan","Cristina","Andres","Sara","Sofia"}

# & inter.
# | union
# - diferencia
# ^ dif. simétrica
print('Quien va a comer y a cenar: ', comida & cena)
print('Quien va solo a comer: ', comida - cena)
print('Quien va solo a cenar: ', cena - comida)
print('Quienes han participado en los eventos: ', comida | cena)
print('Quien va solo a uno de los dos eventos: ', comida ^ cena)

# Va ir Juan a comer?
nombre = 'Raquel'
if nombre in comida:
    print(f'{nombre} va a comer')
else:
    print(f'{nombre} no va a comer')

# Raquel se apunta a comer:
comida.add("Raquel")
comida.add("Raquel")
print(comida)

# Juan no va a cenar:
cena.remove('Juan')
print(cena)

for c  in comida:
    print(c, end=' ')
print()

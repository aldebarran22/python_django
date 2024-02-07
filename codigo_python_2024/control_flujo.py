"""
Bucles: for, while
Condiciones: if else, if compacto
break y continue
"""

# Bucles anidados para imprimir una matriz
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in M:
    for i in fila:
        print(i, end="\t")
    print()

# Dados 2 números comprobar si son iguales, o cual es mayor o menor
n1 = 20
n2 = 20

if n1 < n2:
    print("El menor es: ", n1)
elif n1 == n2:
    print("son iguales")
else:
    print("El mayor es: ", n1)

# if compacto:
# Imprimir "par" si numero es par, y sino impar
numero = 23
print("par" if numero % 2 == 0 else "impar")

# Equivale a
if numero % 2 == 0:
    print("par")
else:
    print("impar")

menor = n1 if n1 < n2 else n2

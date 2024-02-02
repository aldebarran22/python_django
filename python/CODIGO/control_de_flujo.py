"""
Control de flujo: instrucciones condicionales e iterativas
"""

# if else
num1 = 82
num2 = 34
if num1 < num2:
    print(f'{num1} < {num2}')

elif num1 == num2:
    print(f'{num1}=={num2}')

else:
    print(f'{num2} < {num1}')


if num1 == num2:
    print('son iguales')

# if compacto: A if cond else B
numero = 10
print("par" if numero % 2 == 0 else "impar")

menor = num1 if num1 < num2 else num2
print('menor de num1 y num2: ',menor)

print('-' * 10)
print(num1) if num1 < num2 else (print('iguales') \
                                  if num1==num2 else print(num2))
print('-' * 10)

if num1 < num2:
    menor = num1
else:
    menor = num2

# Bucle while:
# imprimir del 1 al 10:

# Con for:
for i in range(1,11):
    print(i, end=' ')
print()

j = 1
while j <= 10:
    print(j, end=' ')
    j += 1  # j = j + 1
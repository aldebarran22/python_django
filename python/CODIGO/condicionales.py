"""
Utilizar un fstring con input y comprobar si una variable
cumple un rango
"""
ini = 10
fin = 50
numero = int(input(f'Teclear valor entre {ini} y {fin}:'))
#if numero >= ini and numero <= fin:
if ini <= numero <= fin:
    print(numero,'cumple el intervalo')
else:
    print(numero,'no cumple el intervalo')


if not (ini <= numero <= fin):
    print(numero, 'no cumple el intervalo')
else:
    print(numero, 'cumple el intervalo')

if numero < ini or numero > fin:
    print(numero, 'no cumple el intervalo')
else:
    print(numero, 'cumple el intervalo')

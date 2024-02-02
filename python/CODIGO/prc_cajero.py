"""

Validación de un número: tiene que ser múltiplo de 10.
importe:> 33
teclear un número múltiplo de 10
importe:> 55
teclear un número múltiplo de 10
importe:> 230
230, ok!

4 de 50
1 de 20
1 de 10
"""
numero = 1
intentos = []
while numero % 10 != 0:
    cad = input('importe:> ')
    if cad.isnumeric():
        numero = int(cad)
        if numero % 10 != 0:
            intentos.append(numero)
            print('teclear un número múltiplo de 10')
    else:
        print('Teclear solo números múltiplo de 10')
        intentos.append(cad)

# El numero es válido  
print(numero,' ok!')
if len(intentos)!=0:        
    print('Te has confundido: ',len(intentos),'veces', intentos)

tipos_billetes = [50,20,10]
billetes = dict()
for b in tipos_billetes:
    if numero >= b:
        numBilletes = numero // b
        billetes[b] = numBilletes
        numero %= b 

    if numero == 0: break


# Imprimir el resultado:
for b, cuenta in billetes.items():
    print(cuenta,'de',b)     

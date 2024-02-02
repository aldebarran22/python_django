"""
Parámetros de la funciones de Python
"""

def ejemploDict(**kwargs):
    print(kwargs)

def calcularIva(importe, iva=0.21):
    return importe * iva

def ejemploArgs(*args):
    print('Has enviado: ', len(args))
    print(args, type(args))
    print()

def segundos(h=0, m=0, s=0):
    return h*3600 + m*60 + s

ejemploDict(x=1, y=2, z=3)

print(segundos())
print(segundos(1,30))
print(segundos(1,1,1))
print(segundos(m=15))
print(segundos(2))
print(segundos(h=2))
print(segundos(s=300))


ejemploArgs()
ejemploArgs(1,2,3,4,5,6,7,8,' ')
ejemploArgs(1)

print(calcularIva(100))
print(calcularIva(100, 0.04))
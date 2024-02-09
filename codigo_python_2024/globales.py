"""
Uso de variables globales en Python
"""
n = 100

def imprimir():
    print("El numero vale: ", n)

def modificar():
    global n
    n += 100 # n = n + 100

if __name__ == '__main__':
    imprimir()
    modificar()
    imprimir()

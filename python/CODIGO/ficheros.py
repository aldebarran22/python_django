"""
Cargar dos ficheros CSV y comparar las lineas
"""

def leerFichero(path):
    f = open(path, "r")
    txt = f.read()
    lineas = txt.split("\n")
    c = set(lineas[1:])
    f.close()
    return c

c = leerFichero("ficheros/fichero1.csv")
print(c)

c2 = leerFichero("ficheros/fichero2.csv")
print(c2)

print("Coincidencias: ", c & c2)
print('lineas del fichero1 que no están en fichero2: ', c-c2)


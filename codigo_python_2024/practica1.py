"""
Cargar el texto del fichero: Contenido.txt
Generar un histograma que nos muestre el número
de veces que se repite cada palabra en texto
"""

# Cargar el fichero:
fich = open("Contenido.txt","r")
txt = fich.read()
fich.close()
# Borrar separadores del texto
txt = txt.replace(",","").replace(".","").replace(";","").replace(":","")
print(txt)

palabras = txt.split(" ")
print('num palabras: ', len(palabras))

palabrasSinRepes = set(palabras)
print('num palabras sin repes: ', len(palabrasSinRepes))

histograma = dict()
for palabra in palabrasSinRepes:
    histograma[palabra] = palabras.count(palabra)
print(histograma)    


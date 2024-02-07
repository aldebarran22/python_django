"""
Cargar el texto del fichero: Contenido.txt
Generar un histograma que nos muestre el número
de veces que se repite cada palabra en texto
"""

# Cargar el fichero:
fich = open("Contenido.txt","r")
txt = fich.read()
fich.close()

txt = txt.replace(",","").replace(".","").replace(";","").replace(":","")
print(txt)
"""
Definición de diccionarios, acceso a los elementos,
añadir nuevas claves y métodos.
Clave inmutable: número, str, tuple
"""

d = {"uno":1, "dos":2, "tres":3}
print("dicc. de ", len(d), 'elementos')

d['uno'] = 100
print(d, type(d))

clases = {"lunes":["C","C++"], 
          "martes":['PHP'],
          "miercoles":["Python","C++"]}

for dia, lenguajes in clases.items(): 
    print(dia, lenguajes)

print(clases['lunes'])
clases['jueves'] = ['PHP', 'Python']
# Añadir SQL al martes:
clases["martes"].append("SQL")
clases['miercoles'].clear()
print(clases)

# range(ini, fin-1, salto=1)

dias = "LMXJV"
numeros = list(range(1,8))
print(numeros)

d2 = dict(zip(dias, numeros))
d2['S'] = 6
print(d2)

d3 = dict(zip(numeros, dias))
print(d3)

# las claves de d3:
print(list(d3.keys()))
# los valores:
print(list(d3.values()))
print(d3[3])

try:
    # Acceso a una clave que no existe: produce la excepción KeyError
    print(d3[30])
except Exception as e:
    print("Se ha producido un error:", e)

print('fin')









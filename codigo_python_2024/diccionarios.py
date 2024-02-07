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

dias = "LMXJVSD"
numeros = list(range(1,8))
print(numeros)

d2 = dict(zip(dias, numeros))
print(d2)

d3 = dict(zip(numeros, dias))
print(d3)







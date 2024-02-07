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






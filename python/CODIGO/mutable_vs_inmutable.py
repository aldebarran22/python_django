"""
Objetos mutables (list, set, dict) vs
Objetos inmutables (tuple, str)
"""

# Objeto mutable, al ordenar la lista el objeto cambia
L = [1,4,3,2,1,5,6,7]
L.sort()
print(L)

# Objeto inmutable al convertir a mayus. un str devuelve un copia:
# El objeto original no cambia!
ciudad = "madrid"
print(ciudad.upper())
print(ciudad) # El objeto original tiene el valor: madrid
# Tenemos que sobrescribir la variable:
ciudad = ciudad.upper()
print(ciudad) # Ya aparece modificada.

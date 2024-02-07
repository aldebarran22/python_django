"""
Conjuntos en Python.
- Quitar repetidos de una lista
- Comprobar si dos listas tienen elementos en común: intersección &
"""
c = {1,3,2,2,2,1,1,4,5,6}
print(c, type(c))

# Quitar repetidos de una lista:
L = [1,2,3] * 4
print(L)
L2 = list(set(L))
print(L2)

persona1 = ['español','inglés','francés']
persona2 = ['alemán', 'inglés','español']
c1 = set(persona1)
c2 = set(persona2)
print('idiomas comunes: ', c1 & c2)

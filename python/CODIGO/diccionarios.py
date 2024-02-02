"""
Diccionarios en python. Crear, recorrer, acceso a elementos

"""

d = {"uno":1, "dos":2, "tres":3}
d['cuatro']=4
d['uno']=1000
print(d, type(d))

d = {"nombre":"Alberto","edad":45,"altura":1.78}
print(d['nombre'])

datos = {"5188800": {"nombre":"Alberto","edad":45,"altura":1.78}}
print(datos['5188800']['nombre'])
datos['5188800']['nombre'] = 'Eva'
print(datos)


L = [1,2,3,4,5]
s = "adios"
d = dict(zip(L, s))
print(d)
d = dict(zip(s, L))
print(d)

# Datos de un alumno: nombre, asignatura y notas
alumno = {"nombre":"Miguel","asignatura":"Excel", "notas":[7.8,4.5,9.9,3]}
# imprimir la ultima:
print(alumno["notas"][-1])

d = {"nombre":"Alberto","edad":45,"altura":1.78}
for k,v in d.items():
    print(k,v, end='\t')
print()

# listas dentro de diccionarios:
d = {"nombre":"Pedro", "notas":[2,6,7,8,10]}
for k,v in d.items():
    if type(v) == list:
        print("Nota media: ", sum(v) / len(v))
    else:
        print(v)

# listas con diccionarios:
L = [{"nombre":"Pedro", "notas":[2,6,7,8,10]},
     {"nombre":"Ana", "notas":[6,6.7,7.1,8,5]},
     {"nombre":"Miguel", "notas":[1,6,7.7,8,6]}]

for d in L:
    print(d['nombre'],sum(d['notas'])/len(d['notas']))

#print(len([2,6,7,8,10]))





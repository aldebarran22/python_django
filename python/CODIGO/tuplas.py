"""
Tuplas en python
Crear tuplas, 
+ * in slicing, índices < 0

select nombre from clientes where pais='Alemania'
select nombre from clientes where pais=?, ('Alemania',)
"""

import math

t1 = 1,2,3,4
t2 = (5,6,7,8)

print(t2[0], t2[-1])
# t2[0] = 1000 Error no soportan asignación.
gps = [(40.4, -3.65),(-36.6, 7.34),(45.6,-12.77)]
for t  in gps:
    print(t, type(t))
    print('latitud: ', t[0])

for latitud, longitud in gps:
    if latitud < 0:
        print(math.fabs(latitud),'S', end = ' ')
    else:
        print(latitud,'N', end = ' ')

    if longitud < 0:
        print(math.fabs(longitud),"W")
    else:
        print(longitud,"E")


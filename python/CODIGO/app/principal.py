"""
Implementación de una clase Hora con el operador +
"""
from modulos.fecha import Fecha
from modulos.hora import Hora
from modulos.fechahora import FechaHora

if __name__=='__main__':
    h1 = Hora(16,15)
    print(h1)
    h2 = Hora(2,55)
    print(h2)
    suma = h1 + h2 # Busca el método especial __add__
    print(suma)
    hoy = Fecha(27,7,2023)
    print(hoy)
    ahora = FechaHora(27,7,2023,17,2)
    print(ahora)
  

    
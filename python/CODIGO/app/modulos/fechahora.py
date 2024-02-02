
from modulos.fecha import Fecha
from modulos.hora import Hora

class FechaHora(Hora, Fecha):
    
    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0):
        Fecha.__init__(self, dd, mm, yy)
        Hora.__init__(self, h, m)

    def __str__(self):
        return Fecha.__str__(self) + " " + Hora.__str__(self)

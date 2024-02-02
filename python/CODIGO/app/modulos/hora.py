class Hora:
    """
    Implementación clase Hora para operaciones de tipo
    h=2, m=5  --> 02:05
    h=16, m=15 -> 16:15
    2:5
    """
    def __init__(self, h=0, m=0):
        self.h = h
        self.m = m

    def __str__(self):
        return "%02d:%02d" % (self.h, self.m)
    
    def __add__(self, otro):
        horas = self.h+otro.h
        minutos = self.m+otro.m
        aux_h = minutos // 60
        horas += aux_h
        minutos %= 60
        return Hora(horas, minutos)
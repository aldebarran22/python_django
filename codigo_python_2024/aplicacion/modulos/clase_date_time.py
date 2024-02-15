try:
    # Para ejecutar el módulo: principal.py
    from modulos.clase_time import Time
    from modulos.clase_date import Date
except:
    # Para ejecutar este módulo
    from clase_time import Time
    from clase_date import Date


class DateTime(Date, Time):

    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0, s=0):
        Date.__init__(self, dd, mm, yy)
        Time.__init__(self, h, m, s)

        # super(Date, Date(dd, mm, yy))
        # super(Time, Time(h, m, s))

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


if __name__ == "__main__":
    dt = DateTime()
    print(dt)

"""
Estructura de los módulos:
principal.py
modulos <dir>
    __init__.py
    clase_time.py       ==> class Time
    clase_date.py       ==> class Date
    clase_date_time.py  ==> class DateTime

"""

from modulos.clase_time import Time

if __name__ == "__main__":
    t = Time(9, 13, 1)
    print(t)

    d = Date(12, 4, 2024)
    print(d)

    # 15/02/2024 18:05:34
    dt = DateTime(15, 2, 2024, 18, 5, 34)
    print(dt)

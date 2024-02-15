class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.h = hh
        self.m = mm
        self.s = ss

    def __str__(self):
        # 9, 13, 1  -> 09:13:01
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)


class Date:

    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.dd, self.mm, self.yy)

    def esBisiesto(self):
        anyo = self.yy
        if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 100 == 0 and anyo % 400 == 0):
            return True
        else:
            return False


class DateTime(Date, Time):
    
    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0, s=0):        
        Date.__init__(self, dd, mm, yy)
        Time.__init__(self, h, m, s)


if __name__ == "__main__":
    t = Time(9, 13, 1)
    print(t)

    # 15/02/2024 18:05:34

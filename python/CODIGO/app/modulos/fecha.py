class Fecha:

    def __init__(self, dd=1,mm=1,yy=1970):
        self.dd=dd
        self.mm=mm
        self.yy=yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.dd, self.mm, self.yy)
    
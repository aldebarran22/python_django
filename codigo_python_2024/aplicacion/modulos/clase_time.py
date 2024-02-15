class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.h = hh
        self.m = mm
        self.s = ss

    def __str__(self):
        # 9, 13, 1  -> 09:13:01
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)

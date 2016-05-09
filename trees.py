class TRee():
    def __init__(self,leftjd = 0,rightjd = 0,data = 0 ):
        self.leftjd = leftjd
        self.rightjd = rightjd
        self.data = data

class Btree():
    def __init__(self,base):
        self.base = base
    def empty(self):
        if self.base is 0:
            return True
        else:
            return False
    def qout(self,jd):
        """NLR"""
        if jd == 0:
            return
        print (jd.data)
        self.qout(jd.leftjd)
        self.qout(jd.rightjd)

    def mout(self,jd):
        """LNR"""
        if jd == 0:
            return
        self.mout(jd.leftjd)
        print (jd.data)
        self.mout(jd.rightjd)

    def hout(self,jd):
        """LRN"""
        if jd == 0:
            return
        self.hout(jd.leftjd)
        self.hout(jd.rightjd)
        print (jd.data)



jd1 = TRee(data =9)
jd2 = TRee(data =8)
base = TRee(jd1, jd2, data=7)
x = Btree(base)
x.qout(x.base)



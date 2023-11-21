import pickle

class SerCls:
    def __init__(self, a, b, c, d):
        self.lst = a
        self.dct = b
        self.num = c
        self.st = d

ser = SerCls([1, 1],{2:'a'},3,"hehe")
s = pickle.dumps(ser)
del ser
del SerCls
class SerCls: pass
ser1 = pickle.loads(s)
print(ser1.st, ser1.num, ser1.dct, ser1.lst)

class Desc :
    def __get__(self, obj, cls) :
        print("GET", repr(obj), cls)
        return obj._value

    def __set__(self, obj, val) :
        print("SET", repr(obj), val)
        obj._value = val

    def __delete__(self, obj) :
        print("Delete", repr(obj))
        obj._value = None

class C :
    data = Desc()

    def __init__(self, numb) :
        self.ata = numb

    def __str__(self) :
        return str(self.data)

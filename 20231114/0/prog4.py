class Desc :
    def __get__(self, obj, cls) :
        print("GET", obj, cls)
        return obj._value

    def __set__(self, obj, val) :
        print("SET", obj, val)
        obj._value = val

class C :
    data = Desc()


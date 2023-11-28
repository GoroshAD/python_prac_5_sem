class ctype(type):

    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        print("prepare", name, bases, kwds)
        return super().__prepare__(name, bases, **kwds)

    @staticmethod
    def __new__(metacls, name, parents, ns, **kwds):
        print("new", metacls, name, parents, ns, kwds)
        return super().__new__(metacls, name, parents, ns)

    def __init__(cls, name, parents, ns, **kwds):
        print("init", cls, parents, ns, kwds)
        return super().__init__(name, parents, ns)

    def __call__(cls, *args, **kwargs):
        print("call", cls, args, kwargs)
        return super().__call__(*args, **kwargs)

class C(int, metaclass=ctype, parameter="See me"):
    field = 42

c = C("100500", base=16)

class sole(type):
    def __new__(metacls, name, prents, namespace):
        if len(parents) > 1:
            raise TypeError("Two or more parents!!")
        return super().__new__(metacls, name, parents, namespace)


class final(type):
    def __new__(metacls, name, parents, namespace):
        for cls in parents:
            if isinstance(cls, final):
                raise TypeError(f"{cls.__name__} is final")
        return super().__new__(metacls, name, parents, namespace)
class E(metaclass=final): pass
class C: pass
class A(C, E): pass

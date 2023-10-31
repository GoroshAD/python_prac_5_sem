class Omnibus :
    attr_counter = {}

    def __setattr__(self, name, mean) :
        if name in Omnibus.attr_counter.keys() :
            Omnibus.attr_counter[name] += 1
        else :
            Omnibus.attr_counter[name] = 1
        #self.__dict__[name] = Omnibus.attr_counter[name]
        pass
    
    def __getattr__(self, name) :
        return Omnibus.attr_counter[name]

    def __delattr__(self, name) :
        if name in Omnibus.attr_counter.keys() :
            Omnibus.attr_counter[name] -= 1
        pass

a, b, c = Omnibus(), Omnibus(), Omnibus()
del a.random
a.i = a.j = a.k = True
b.j = b.k = b.n = False
c.k = c.n = c.m = hex
print(a.i, a.j, a.k, b.j, b.k, b.n, c.k, c.n, c.m)
del a.k, b.n, c.m
print(a.i, a.j, b.j, b.k, c.k, c.n)
del a.k, c.m
print(a.i, a.j, b.j, b.k, c.k, c.n)
a.k = b.i = c.m = 777
print(a.i, a.j, a.k, b.j, b.k, c.k, c.n, c.m) 
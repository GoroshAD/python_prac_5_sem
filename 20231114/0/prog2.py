def intchk(typ) :
    def checker(fun) :
        def newfun(*args) :
            for i in (args) :
                if type(i) != typ :
                    raise TypeError
            return 
        return newfun
    return checker

@intchk(int)
def fun(a, b, c, d, e) :
    a + b + c + d + e
    return


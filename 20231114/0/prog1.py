def checker(fun) :
    def newfun(*args) :
        for i in (args) :
            if type(i) != int :
                raise TypeError
        return 
    return newfun

@checker
def fun(a, b, c, d, e) :
    a + b + c + d + e
    return


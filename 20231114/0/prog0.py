def genf(f):
    def newfun(*args):             
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

@genf
def fun(a,b):
    return a*2+b

print(fun(2,3))


from functools import wraps

def debug(f) :
    @wraps(fun)
    def wrapper(*args) :
        print("<", *args)
        res = f(*args)
        print(">", res)
        return res
    return wrapper

@debug
def mult(a, b) :
    '''this is mult'''
    return a * b
print(mult, mult.__doc__)

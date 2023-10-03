def sub(a, b) :
    if type(a) != type(b) :
        return "ERROR"
    if type(a) in (tuple, list) :
        return type(a)(i for i in a if not i in b)
    else :
        return a - b

print(sub(*eval(input())))

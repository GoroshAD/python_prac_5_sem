from math import *

def div_ab(a, b) :
    try :
        res = a / b
    except ZeroDivisionError :
        res = inf
    return res

for i in ((10,2),(1,0),(9,3)) :
    print(div_ab(*i))

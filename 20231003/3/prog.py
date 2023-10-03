def Calc(s, t, u) :
    f, g, h = lambda x: eval(s), lambda x: eval(t), lambda x, y: eval(u)
    def fun(*args) :
        return h(f(*args), g(*args))
    return fun

from math import *
s,t,u = eval(input())
F = Calc(s, t, u)
x = eval(input())
print(F(x))

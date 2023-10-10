from decimal import *
from fractions import *

def multiplier(x, y, Type) :
    return Type(x) * Type(y)

print(multiplier(*eval(input()), eval(input())))

from decimal import *

def esum(N, one) :
    if type(one) == Decimal :
        sum = Decimal(1)
        factor = 1
        for i in range(1, N + 1) :
            sum += Decimal(1) / Decimal(factor * i)
            factor *= i
        return sum
    else :
        sum = 1.0
        factor = 1
        for i in range(1, N + 1) :
            sum += 1 / (factor * i)
            factor *= i
        return sum

getcontext().prec = int(input())
print(esum(1000, Decimal(1)))
print(esum(100, 1.0))

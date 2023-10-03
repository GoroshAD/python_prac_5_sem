def lin(a, b) :
    return lambda x: a * x + b

print(lin(*eval(input()))(8))

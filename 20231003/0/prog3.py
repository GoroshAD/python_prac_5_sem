def fun(a):
    if a > 0:
        print(a)
        return fun(a-1)
    return 0
print(fun(100))

def h(f, g):
    return lambda x : f(x) + g(x)

print(h(max, min)(eval(input())))

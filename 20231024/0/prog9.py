from itertools import product

print(list(f"{c[0]}{c[1]}" for c in product("ABCDEFGH", "12345678")))
#list(product(*[range(3)] * 13))

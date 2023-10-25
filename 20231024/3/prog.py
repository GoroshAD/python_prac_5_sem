from itertools import product, filterfalse
print(*sorted(list(filterfalse(lambda x : x.count("TOR") != 2 ,("".join(i) for i in list(product("TOR", repeat = eval(input()))))))))

from itertools import product, filterfalse
print(*sorted(list(filter(lambda x : x.count("TOR") == 2 ,("".join(i) for i in list(product("TOR", repeat = eval(input()))))))))

import itertools as it

def ffn(n, seq) :
    yield from it.filterfalse(lambda x : not x % n, seq)

print(list(ffn(3, range(21))))

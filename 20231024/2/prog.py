import itertools as it

def slide(seq, n) :
    i = 0
    a = list(it.islice(seq, i, n))
    while (a) :
        i += 1
        yield a
        a = list(it.islice(seq, i, n + i))

print(*list(slide(range(5), 3)))

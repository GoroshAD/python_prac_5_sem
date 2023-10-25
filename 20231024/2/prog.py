import itertools as it

def slide(seq, n) :
    i = 0
    a = list(it.islice(seq, i, n))
    while (a) :
        i += 1
        for j in a :
            yield j
        a = list(it.islice(seq, i, n + i))

import sys
exec(sys.stdin.read())

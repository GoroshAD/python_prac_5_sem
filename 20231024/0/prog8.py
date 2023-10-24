import itertools as it

def repeater(seq, n) :
    for i in seq :
        yield from it.repeat(i, n)

print(list(repeater("abracadabra", 3)))

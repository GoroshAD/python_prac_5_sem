from itertools import repeat

def travel(n) :
    yield from repeat("po kouchkam", n)
    return "i v yamu"

def travelwrap(n) :
    res = yield from travel(n)
    yield res

def travel(n) :
    for i in range(n) :
        yield "по кочкам"
    return "и в яму"

def travelwrap(n) :
    res = yield from travel(n)
    yield res #это обязательно из-за return, так как без этого он не выводится

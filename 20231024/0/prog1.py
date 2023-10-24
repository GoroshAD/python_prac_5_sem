from itertools import count

def func() :
    s = 0
    for i in count(1) :
        yield (s := s + 1 / i**2)


s = func()
print(next(s))
print(next(s))

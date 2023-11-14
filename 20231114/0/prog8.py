class R :
    pass

class S :
    __slots__ = ["x"]

s = S()
r = R()
r.x = 100500
s.x = 100500
import sys
print(sys.getsizeof(r))
print(sys.getsizeof(s))

class S :
    __slots__ = ["x"]
    def __init__(self, val) :
        self.x = val
class R :
    def __init__(self, val) :
        self.x = val
from pympler import asizeof
rl = [R(i) for i in range(1000)]
sl = [S(i) for i in range(1000)]
print(asizeof.asizeof(rl))
print(asizeof.asizeof(sl))

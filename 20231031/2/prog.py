from itertools import permutations

class Triangle :
    def side_func(self, x1, x2, x3) :
        k = (x2[1] - x1[1]) / (x2[0] - x1[0]) if x2[0] != x1[0] else 0
        b = x2[1] - x2[0] * k
        return 0 if (x3[1] == x3[0] * k + b and x3[0] <= max(x2[0], x1[0]) and x3[0] >= min(x2[0], x1[0])) else 1 if x3[1] > x3[0] * k + b else -1

    def inside(self, z) :
        ao, bo, co = (- self.x[0] + z[0], z[1] - self.x[1]), (z[0] - self.y[0], z[1] - self.y[1]), (z[0] - self.z[0], z[1] - self.z[1])
        oa, ob, oc = (-ao[0], -ao[1]), (-bo[0], -bo[1]), (-co[0], -co[1])
        return all((ao[0] * ob[1] - ao[1] * ob[0] >= 0, bo[0] * oc[1] - bo[1] * oc[0] >= 0, co[0] * oa[1] - co[1] * oa[0] >= 0)) or \
                all((ao[0] * ob[1] - ao[1] * ob[0] <= 0, bo[0] * oc[1] - bo[1] * oc[0] <= 0, co[0] * oa[1] - co[1] * oa[0] <= 0))


    def __init__(self, a, b, c) :
        self.x, self.y, self.z = tuple(a), tuple(b), tuple(c)
        self.a = ((self.x[0] - self.y[0])**2 + (self.x[1] - self.y[1])**2)**(0.5)
        self.b = ((self.z[0] - self.y[0])**2 + (self.z[1] - self.y[1])**2)**(0.5)
        self.c = ((self.x[0] - self.z[0])**2 + (self.x[1] - self.z[1])**2)**(0.5)
        pass

    def __abs__(self) :
        if not self :
            return 0
        self.p = (self.a + self.b + self.c) / 2.0
        return round((self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))**(0.5), 3)
    
    def __bool__(self) :
        return all((self.a + self.b > self.c, self.a + self.c > self.b, self.b + self.c > self.a))
    
    def __lt__(self, other) :
        return abs(self) < abs(other)
    
    def __contains__(self, other) :
        if abs(self) == 0 :
            return True
        if abs(other) == 0 :
            return True
        return all((self.inside(other.x), self.inside(other.y), self.inside(other.z)))
    
    def __and__(self, other) :
        if abs(self) == 0 or abs(other) == 0 :
            return False
        if self in other or other in self :
            return True
        for i in permutations((self.x, self.y, self.z), 2) :
            for j in permutations((other.x, other.y, other.z), 2) :
                a, b, c, d = self.side_func(*i, j[0]), self.side_func(*i, j[1]), self.side_func(*j, i[0]), self.side_func(*j, i[1])
                if a * b * c * d == 0 :
                    return True
                if a * b < 0 and c * d < 0:
                    return True
        return False       
        
import sys
exec(sys.stdin.read())

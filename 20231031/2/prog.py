class Triangle :
    def inside(self, z) :
        ao, bo, co = (- self.x[0] + z[0], z[1] - self.x[1]), (z[0] - self.y[0], z[1] - self.y[1]), (z[0] - self.z[0], z[1] - self.z[1])
        oa, ob, oc = (-ao[0], -ao[1]), (-bo[0], -bo[1]), (-co[0], -co[1])
        return all((ao[0] * ob[1] - ao[1] * ob[0] > 0, bo[0] * oc[1] - bo[1] * oc[0] > 0, co[0] * oa[1] - co[1] * oa[0] > 0)) or \
                all((ao[0] * ob[1] - ao[1] * ob[0] < 0, bo[0] * oc[1] - bo[1] * oc[0] < 0, co[0] * oa[1] - co[1] * oa[0] < 0))


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
        return (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))**(0.5)
    
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
        if any((self.x == other.x, self.y == other.y, self.z == other.z, \
                self.x == other.y, self.y == other.z, self.z == other.x, \
                self.x == other.z, self.y == other.x, self.z == other.y)) :
            return True
        return any((any((self.inside(other.x) != self.inside(other.y) == self.inside(other.z), \
                   self.inside(other.x) == self.inside(other.y) != self.inside(other.z), \
                   self.inside(other.x) == self.inside(other.z) != self.inside(other.y))), \
                   any((other.inside(self.x) != other.inside(self.y) == other.inside(self.z), \
                   other.inside(self.x) == other.inside(self.y) != other.inside(self.z), \
                   other.inside(self.x) == other.inside(self.z) != other.inside(self.y)))))
            
        
import sys
exec(sys.stdin.read())
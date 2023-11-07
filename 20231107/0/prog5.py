class A : 
    def __init__(self, var) :
        self.var = var

class B(A) : 
    def __init__(self, var) :
        super().__init__(var)
        self.otver = var * 2

b = B(12)
print(b.var)
print(b.otver)



class A : 
    def __str__(self) :
        return "A"

class B(A) :
    def __str__(self) :
        return super().__str__() + " : B"
class C(B) : 
    def __str__(self) :
        return super().__str__() + " : C"

c = C()
print(c)



class A :
    def __init__(self, var) :
        self.var = var
        pass

    def __add__(self, number) :
        return A(self.var + number)

a = A(1)
print(a)
print(a.var)
print((a+1).var)
class B(A) :
    def __str__(self) :
        return f"<{self.var}>"

a = B(12)
print(a)
print(a + 1)
type(a + 1)
print(B.mro())
#recommend:
class A :
    def __init__(self, var) :
        self.var = var
        pass

    def __add__(self, number) :
        return self.__class__(self.var + number)
class B(A) :
    def __str__(self) :
        return f"<{self.var}>"

a = B(12)
print(a + 1)

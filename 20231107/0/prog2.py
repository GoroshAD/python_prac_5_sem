class A :
    f = 1
    def __str__(self) :
        return f"{self.f}"

class B(A) :
    def __init(self) :
        self.f = 100500

print(A())
print(B())

class A :
    __f = 1
    def __str__(self) :
        return f"{self.__f}"

class B(A) :
    def __init__(self) :
        self.__f = 100500

print(B())
print(A.__dict__)
print(B.__dict__)


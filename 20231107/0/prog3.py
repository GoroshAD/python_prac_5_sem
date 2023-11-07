class A : pass
class B(A) : pass
#class X(A, B) : pass      - error
class Y(B, A) : pass
print(Y.mro())


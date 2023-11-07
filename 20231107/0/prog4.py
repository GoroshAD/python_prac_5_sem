class A : pass
class B : pass

class C(A, B) : pass
class D(B, A) : pass

#class E(C, B, A) : pass     - error
#class E(A, C) : pass     - error
#class E(B, C) : pass     - error

class E(C, A, B) : pass   # - OK
class E(C, A) : pass   # - OK
class E(C, B) : pass   # - OK

class A(Exception) :
    pass

class B(A) :
    pass

class C(B) :
    pass

for E in (A, B, C) :
    try :
        raise E
    except B :
        print("B")
    except A :
        print("A")
    except C : 
        print("C")

while True :
    try :
        res = int(input())
    except Exception :
        print("Again...")
    else :
        print("Finally!", res)
        break


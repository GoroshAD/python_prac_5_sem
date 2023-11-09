from math import *

class InvalidInput(Exception) : pass
class BadTriangle(Exception) : pass

def triangleSquare(inStr) :
    try : 
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except Exception :
        raise InvalidInput
    try :
        a = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        b = sqrt((x2 - x3)**2 + (y2 - y3)**2)
        c = sqrt((x3 - x1)**2 + (y3 - y1)**2)
        p = (a + b + c) / 2
        if any((a + b <= c, a + c <= b, b + c <= a)) : 
            raise BadTriangle
        sq = sqrt(p * (p - a) * (p - b) * (p - c))
    except Exception :
        raise BadTriangle
    return sq
    

while True :
    try :
        inStr = input()
        sq = triangleSquare(inStr)
    except InvalidInput :
        print("Invalid input")
    except BadTriangle :
        print("Not a triangle")
    else :
        print(f'{sq:.2f}')
        break

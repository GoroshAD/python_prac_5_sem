from collections import UserString

class DivStr(UserString) :
    def __init__(self, data = "") :
        super().__init__(data)

    def __floordiv__(self, number) :
        k = len(self.data) // number
        return (self.data[i * k : (i + 1) * k] for i in range(number))

    def __mod__(self, number):
        r = len(self.data) % number
        return DivStr(self.data[-r :]) if r != 0 else DivStr()

import sys
exec(sys.stdin.read())

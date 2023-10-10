from math import *
import prog4

src = [[' ']*60 for i in range(20)]
for i in range(60) :
    x = prog4.scale(0, 59, 0, 7, i)
    y = sin(x)
    w = prog4.scale(-1, 1, 0, 20, y)
    src[int(w)][int(x)] = '*'
print("\n".join(["".join(s) for s in src]))

from math import *

s = []
while (x := input()) :
    s.append(x)
n, m = len(s), len(s[0])
wat_len = m - 2
wat_hei = 0
for i in range(n) :
    if "." in s[i] :
        wat_air = i
wat_hei = n - 2 - wat_air
wat_vol = wat_hei * wat_len

new_wat_len = n - 2
new_wat_hei = int(wat_vol / new_wat_len) + bool((wat_vol / new_wat_len) % 1)

src = [["#"] * n for i in range(m)]
for i in range(m) :
    if i != 0 and i != m - 1 :
        flag = False if i > m - 2 - new_wat_hei else True
        for j in range(1, n - 1) :
            src[i][j] = "." if flag else "~"
for i in src :
    print("".join(i))

vol = (n - 2) * (m - 2)
wat = new_wat_hei * new_wat_len
air = vol - wat

if air > wat :
    s = "".join(["." for i in range(20)])
    n = round(20 * wat / air)
    a = "".join(["~" for i in range(n)])
    out = " " + str(air) + "/" + str(vol)
    print("{}{}".format(s, out))
    out = str(wat) + "/" + str(vol)
    n = 21 - n + 1 + max(len(str(wat)), len(str(air))) + len(str(vol))
    print("{}{:>{}}".format(a, out, n))
else :
    s = "".join(["~" for i in range(20)])
    n = round(20 * air / wat)
    a = "".join(["." for i in range(n)])
    out = str(air) + '/' + str(vol)
    n = 21 - n + 1 + max(len(str(wat)), len(str(air))) + len(str(vol))
    print("{}{:>{}}".format(a, out, n))
    out = " " + str(wat) + '/' + str(vol)
    print("{}{}".format(s, out))


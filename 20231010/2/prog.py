from math import *

def count_stars_down(src, j, i, H) :
    for k in range(i + 1, H) :
        if (src[k][j] == "*") or (j != 0 and src[k][j - 1] == "*") or (j != W - 1 and src[k][j + 1] == "*") :
            return True
    return False

def count_stars_upper(src, i, j, H, W) :
    counter = 0
    if (i != 0) :
        counter += 1 if src[i - 1][j] == "*" else 0
        if (j != 0) :
            counter += 1 if src[i - 1][j - 1] == "*" else 0
        if (j != W - 1) :
            counter += 1 if src[i - 1][j + 1] == "*" else 0
    if (i != H - 1) :
        counter += 1 if src[i + 1][j] == "*" else 0
        if (j != 0) :
            counter += 1 if src[i + 1][j - 1] == "*" else 0
        if (j != W - 1) :
            counter += 1 if src[i + 1][j + 1] == "*" else 0
    if (j != 0) :
        counter += 1 if src[i][j - 1] == "*" else 0
    if (j != W - 1) :
        counter += 1 if src[i][j + 1] == "*" else 0
    return counter


W, H, A, B, s = map(str, input().split())
W, H, A, B = eval(W), eval(H), eval(A), eval(B)
f = lambda x : eval(s)

def scale(a, b, A, B, x) :
    return (x - a) * (B - A) / (b - a) + A

src = [[" "]*W for i in range(H)]
min_n, max_n = None, None
for i in range(W) :
    x = scale(0, W - 1, A, B, i)
    y = f(x)
    if min_n == None or min_n > y :
        min_n = y
    if max_n == None or max_n < y :
        max_n = y

for i in range(W) :
    x = scale(0, W - 1, A, B, i)
    y = f(x)
    w = round(scale(min_n, max_n, H - 1, 0, y))
    src[w][i] = "*"

for i in range(H) :
    for j in range(W) :
        if i != 0 and src[i - 1][j] == "*" :
            if (j == 0 or j == W - 1) and not count_stars_down(src, j, i, H) :
                continue
            if count_stars_upper(src, i - 1, j, H, W) >  1 :
                continue
            if (j == 0) :
                if src[i][j + 1] != "*" :
                    src[i][j] = "*"
            elif (j == W - 1) :
                if src[i][j - 1] != "*" :
                    src[i][j] = "*"
            elif src[i][j + 1] != "*" and src[i][j - 1] != "*" :
                src[i][j] = "*"
print("\n".join("".join(s) for s in src))



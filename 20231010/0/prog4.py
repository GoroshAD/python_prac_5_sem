from math import *

def scale(a, b, A, B, x) :
    return (x - a) * (B - A)/ (b - a) + A

def sinus(N, n) :
    for i in range(-n, n) :
        x = scale(0, N - 1, -n, n, i)
        print(" "*int((sin(x) + 1) * 10), "*")

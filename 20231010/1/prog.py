import fractions as fr

s, w, *a = map(fr.Fraction, input().split(", "))

A_n, a = int(a[0]), a[1:]
A = fr.Fraction(0)
for i in range(A_n, -1, -1) :
    A += fr.Fraction(s**i * a[0])
    a = a[1:]

B_n, a = int(a[0]), a[1:]
B = fr.Fraction(0)
for i in range(B_n, -1, -1) :
    B += fr.Fraction(s**i * a[0])
    a = a[1:]

print(fr.Fraction(A, B) == fr.Fraction(w)) if B else print(False)

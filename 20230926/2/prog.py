def key(a):
    return a**2 % 100

a = list(eval(input()))
for i in range(1, len(a)):
    remem = i
    while i > 0 and key(a[i-1]) > key(a[i]):
        a[i - 1], a[i] = a[i], a[i - 1]
        i -= 1
    i = remem
print(a)

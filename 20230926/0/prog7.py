a = []
while s:= input():
    a.append(eval(s))
n = len(a)
if all([len(i) == n for i in a]):
    print("yes")
else:
    print("no")
for i in range(n):
    for j in range(i, n):
        a[i][j], a[j][i]  = a[j][i], a[i][j]
for i in range(n):
    for j in range(n):
        print(a[i][j], end =" ")
    print()

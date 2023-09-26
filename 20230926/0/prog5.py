a = []
while (b := input()):
    a.append(eval(b))

for i in range(len(a)):
    for j in range(i, len(a[i])):
        a[i][j], a[j][i] = a[j][i], a[i][j]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = " ")
    print()

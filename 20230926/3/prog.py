a1, a2 = [], []
if s := eval(input()):
    n = len(s)
    a1.append(s)
    for i in range(n - 1):
        a1.append(eval(input()))
    for i in range(n):
        a2.append(eval(input()))
    res = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for a in range(n):
                res[i][j] += a1[i][a] * a2[a][j]
    for i in range(n):
            print(*res[i], sep = ",")

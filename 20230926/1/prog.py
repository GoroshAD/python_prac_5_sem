m, n = eval(input())
print([i for i in range(m, n) if all(((i % j or i == j) and i != 1) for j in range(2, int(i**(1/2)) + 2))])

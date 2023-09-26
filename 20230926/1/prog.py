m, n = eval(input())
print([i for i in range(m, n) if all((i != 1 and (i % j or i == j)) for j in range(2, round(i**(1/2)) + 2))])

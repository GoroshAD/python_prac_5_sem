a, b, c = eval(input())
print(min(a, b, c) > 0 and a < (b + c) and b < (a + c) and c < (a + b))

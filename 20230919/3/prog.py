x = eval(input())
n1 = n2 = x
while n1 <= x + 2:
    while n2 <= x + 2:
        a = n1*n2
        counter = 0
        while a > 0:
            counter += a % 10
            a = a // 10
        print(n1," * ",n2," = ", ":=)" if counter == 6 else n1*n2, end = " ")
        n2 += 1
    print()
    n1 += 1
    n2 = x

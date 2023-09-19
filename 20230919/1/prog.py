x = eval(input())
print("A", "+" if (x % 2 == 0 and x % 25 == 0) else "-", end = " ")
print("B", "+" if (x % 2 == 1 and x % 25 == 0) else "-", end = " ")
if x % 8 == 0 : 
    print("C +") 
else: 
    print("C -")

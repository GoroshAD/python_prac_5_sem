class C:
    a, b, c = input("a, b, c: ").split()

while ne := input().split():
    match ne:
        case [C.a, *other] if "yes" in other:
            print(1)
        case [C.b]:
            print(2)
        case [C.c, *kw, C.b]:
            print(3)
        case _:
            print("no.")


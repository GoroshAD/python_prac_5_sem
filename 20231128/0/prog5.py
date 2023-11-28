while x := list(input().split()):
    match x[0]:
        case "mov":
            print("moving {} to {}".format(x[1], x[0]))
        case "push" | "pop":
            print("{}ing ".format(x[0]), *x[1:])
        case _:
            print("making {} with {}".format(x[0], x[1]))

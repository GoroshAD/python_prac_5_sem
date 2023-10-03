def Pareto(*args):
    def checker(a,b):
        if a[0] <= b[0] and a[1] <= b[1] and (a[0] < b[0] or a[1] < b[1]):
            return False
        return True

    res = []
    for i in range(len(args)): 
        flag = True
        for j in range(len(args)):
            if not checker(args[i], args[j]):
                flag = False
        if flag:
            res.append(args[i])
    return res         


a = list(eval(input()))
print(tuple(Pareto(*a)))

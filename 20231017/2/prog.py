from math import *

dict, counter = {}, 0
while (x := input()) :
    if x[0] == ":" :
        x = x[1:].split()
        dict[x[0]] = x[1:]
        counter += 1
    else :
        if len(x) >= 4 and x[:4] == "quit" :
            x = x[4:]
            counter += 1
            print(eval(x).format(len(dict) + 1, counter))
            break
        else :
            x = x.split()
            print(eval(dict[x[0]][-1], globals(), {dict[x[0]][i - 1] : eval(x[i]) for i in range(1, len(dict[x[0]]))}))
            counter += 1

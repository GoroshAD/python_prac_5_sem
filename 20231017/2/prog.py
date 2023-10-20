from math import *

def parser(x) :
    a, flag_bracket, flag_quotation = [], 0, 0
    tmp = []
    for i in range(len(x)) :
        if x[i] != " " or flag_bracket or flag_quotation :
            tmp.append(x[i])
        else :
            if tmp != []:
                a.append("".join(tmp))
            tmp =[]
        if x[i] in ["[", "{", "("] :
            flag_bracket += 1
        if x[i] in ["'", '"'] :
            flag_quotation += 1
        if x[i] in ["]", "}", ")"] :
            flag_bracket -= 1
        if x[i] in ["'", '"'] :
            flag_quotation -= 1
    if tmp != [] :
        a.append("".join(tmp))
    return a

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
            x = parser(x)
            print(eval(dict[x[0]][-1], globals(), {dict[x[0]][i - 1] : eval(x[i]) for i in range(1, len(dict[x[0]]))}))
            counter += 1

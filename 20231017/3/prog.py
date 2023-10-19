n = eval(input())
dict = {}
while (x := list(input())) :
    for i in range(len(x)) :
        if not x[i].isalpha() :
            x[i] = " "
    x = "".join(x).split()
    for i in x :
        if len(i) == n :
            if i in dict.keys() :
                dict[i] += 1
            else :
                dict[i] = 1

if len(dict) :
    maxed_words = []
    max_n = max((zip(dict.values(), dict.keys())))[0]
    for i in dict.keys() :
        if dict[i] == max_n :
            maxed_words.append(i)
    print(*maxed_words)


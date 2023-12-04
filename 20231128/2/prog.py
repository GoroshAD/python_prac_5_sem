import math, sys

vals_dict = {}
marks_dict = {}
marks_appear = set()
marks_exactly = set()

def interpretator_check():
    file = sys.stdin.readlines()
    fil = []
    i = 0
    while (i < len(file)) and file[i].split() != ['stop']:
        s = file[i]
        s = s.split()
        if len(s) < 1:
            i += 1
            continue
        if s[0][-1] == ':':
            marks_dict[s[0][:-1]] = file[i:]
            marks_exactly.add(s[0][:-1])
            if len(s[1:]) < 1:
                i += 1
                continue
            match s[1]:
                case 'store':
                    if len(s) != 4:
                        i += 1
                        continue
                    fil.append(s)
                case 'div' | 'sub' | 'mul' | 'add':
                    if len(s) != 5:
                        i += 1
                        continue
                    fil.append(s)
                case 'ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle':
                    marks_appear.add(s[4])
                    if len(s) != 5:
                        i += 1
                        continue
                    fil.append(s)
                case 'out':
                    if len(s) != 3:
                        i += 1
                        continue
                    fil.append(s)
        match s[0]:
            case 'store':
                if len(s) != 3:
                    i += 1
                    continue
                fil.append(s)
            case 'div' | 'sub' | 'mul' | 'add':
                if len(s) != 4:
                    i += 1
                    continue
                fil.append(s)
            case 'ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle':
                marks_appear.add(s[3])
                if len(s) != 4:
                    i += 1
                    continue
                fil.append(s)
            case 'out':
                if len(s) != 2:
                    i += 1
                    continue
                fil.append(s)
        i += 1

    for i in marks_appear:
        if not i in marks_exactly:
            return False

    for i in marks_dict.keys():
        tmp = []
        arr = marks_dict[i]
        for s in arr:
            s = s.split()
            if s == ['stop']:
                break
            if len(s) < 1:
                continue
            if s[0][-1] == ':':
                if len(s) < 2:
                    continue
                match s[1]:
                    case 'add' | 'div' | 'mul' | 'sub':
                        if len(s) == 5:
                            tmp.append(s)
                    case 'ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle':
                        if len(s) == 5:
                            tmp.append(s)
                    case 'out':
                        if len(s) == 3:
                            tmp.append(s)
                    case 'store':
                        if len(s) == 4:
                            tmp.append(s)
            match s[0]:
                case 'add' | 'div' | 'mul' | 'sub':
                    if len(s) == 4:
                        tmp.append(s)
                case 'ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle':
                    if len(s) == 4:
                        tmp.append(s)
                case 'out':
                    if len(s) == 2:
                        tmp.append(s)
                case 'store':
                    if len(s) == 3:
                        tmp.append(s)
        marks_dict[i] = tmp
    return fil
                
def interpretator_func(fil):
    i = 0
    while (i < len(fil)):
        s = fil[i]
        if s[0][-1] == ':':
            s = s[1:]
        match s[0]:
            case 'out':
                if s[1] in vals_dict.keys():
                    print(vals_dict[s[1]])
                else:
                    try:
                        print(float(eval(s[2])))
                    except:
                        print(0)
            case 'div':
                tmp1, tmp2 = 0, 0
                try:
                    if s[1] in vals_dict.keys():
                        tmp1 = vals_dict[s[1]]
                    else:
                        tmp1 = float(eval(s[1]))
                except:
                    tmp1 = 0
                try:
                    if s[2] in vals_dict.keys():
                        tmp2 = vals_dict[s[2]]
                    else:
                        tmp2 = float(eval(s[2]))
                except:
                    tmp2 = 0
                try:
                    vals_dict[s[3]] = tmp1 / tmp2
                except:
                    vals_dict[s[3]] = math.inf
            case 'mul':
                tmp1, tmp2 = 0, 0
                try:
                    if s[1] in vals_dict.keys():
                        tmp1 = vals_dict[s[1]]
                    else:
                        tmp1 = float(eval(s[1]))
                except:
                    tmp1 = 0
                try:
                    if s[2] in vals_dict.keys():
                        tmp2 = vals_dict[s[2]]
                    else:
                        tmp2 = float(eval(s[2]))
                except:
                    tmp2 = 0
                vals_dict[s[3]] = tmp1 * tmp2
            case 'add':
                tmp1, tmp2 = 0, 0
                try:
                    if s[1] in vals_dict.keys():
                        tmp1 = vals_dict[s[1]]
                    else:
                        tmp1 = float(eval(s[1]))
                except:
                    tmp1 = 0
                try:
                    if s[2] in vals_dict.keys():
                        tmp2 = vals_dict[s[2]]
                    else:
                        tmp2 = float(eval(s[2]))
                except:
                    tmp2 = 0
                vals_dict[s[3]] = tmp1 + tmp2
            case 'sub':
                tmp1, tmp2 = 0, 0
                try:
                    if s[1] in vals_dict.keys():
                        tmp1 = vals_dict[s[1]]
                    else:
                        tmp1 = float(eval(s[1]))
                except:
                    tmp1 = 0
                try:
                    if s[2] in vals_dict.keys():
                        tmp2 = vals_dict[s[2]]
                    else:
                        tmp2 = float(eval(s[2]))
                except:
                    tmp2 = 0
                vals_dict[s[3]] = tmp1 - tmp2
            case 'ifeq':
                tmp1, tmp2 = 0, 0
                try:
                    if s[1] in vals_dict.keys():
                        tmp1 = vals_dict[s[1]]
                    else:
                        tmp1 = float(eval(s[1]))
                except:
                    tmp1 = 0
                try:
                    if s[2] in vals_dict.keys():
                        tmp2 = vals_dict[s[2]]
                    else:
                        tmp2 = float(eval(s[2]))
                except:
                    tmp2 = 0
                if tmp1 == tmp2:
                    i = 0
                    fil = marks_dict[s[3]]
                    continue
            case 'ifne':
                tmp1, tmp2 = 0, 0
                try:
                    if s[1] in vals_dict.keys():
                        tmp1 = vals_dict[s[1]]
                    else:
                        tmp1 = float(eval(s[1]))
                except:
                    tmp1 = 0
                try:
                    if s[2] in vals_dict.keys():
                        tmp2 = vals_dict[s[2]]
                    else:
                        tmp2 = float(eval(s[2]))
                except:
                    tmp2 = 0
                if tmp1 != tmp2:
                    i = 0
                    fil = marks_dict[s[3]]
                    continue
            case 'ifgt':
                tmp1, tmp2 = 0, 0
                try:
                    if s[1] in vals_dict.keys():
                        tmp1 = vals_dict[s[1]]
                    else:
                        tmp1 = float(eval(s[1]))
                except:
                    tmp1 = 0
                try:
                    if s[2] in vals_dict.keys():
                        tmp2 = vals_dict[s[2]]
                    else:
                        tmp2 = float(eval(s[2]))
                except:
                    tmp2 = 0
                if tmp1 > tmp2:
                    i = 0
                    fil = marks_dict[s[3]]
                    continue
            case 'ifge':
                tmp1, tmp2 = 0, 0
                try:
                    if s[1] in vals_dict.keys():
                        tmp1 = vals_dict[s[1]]
                    else:
                        tmp1 = float(eval(s[1]))
                except:
                    tmp1 = 0
                try:
                    if s[2] in vals_dict.keys():
                        tmp2 = vals_dict[s[2]]
                    else:
                        tmp2 = float(eval(s[2]))
                except:
                    tmp2 = 0
                if tmp1 >= tmp2:
                    i = 0
                    fil = marks_dict[s[3]]
                    continue
            case 'iflt':
                tmp1, tmp2 = 0, 0
                try:
                    if s[1] in vals_dict.keys():
                        tmp1 = vals_dict[s[1]]
                    else:
                        tmp1 = float(eval(s[1]))
                except:
                    tmp1 = 0
                try:
                    if s[2] in vals_dict.keys():
                        tmp2 = vals_dict[s[2]]
                    else:
                        tmp2 = float(eval(s[2]))
                except:
                    tmp2 = 0
                if tmp1 < tmp2:
                    i = 0
                    fil = marks_dict[s[3]]
                    continue
            case 'ifle':
                tmp1, tmp2 = 0, 0
                try:
                    if s[1] in vals_dict.keys():
                        tmp1 = vals_dict[s[1]]
                    else:
                        tmp1 = float(eval(s[1]))
                except:
                    tmp1 = 0
                try:
                    if s[2] in vals_dict.keys():
                        tmp2 = vals_dict[s[2]]
                    else:
                        tmp2 = float(eval(s[2]))
                except:
                    tmp2 = 0
                if tmp1 <= tmp2:
                    i = 0
                    fil = marks_dict[s[3]]
                    continue
            case 'store':
                try:
                    vals_dict[s[2]] = float(eval(s[1]))
                except:
                    vals_dict[s[2]] = 0
        i += 1
            

if fil := interpretator_check():
    interpretator_func(fil)
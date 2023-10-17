import timeit as tm
import string as string

def count(str) :
    str.lower()
    vow = set(['e', 'y', 'u', 'i', 'o', 'a'])
    con = set(string.ascii_lowercase) - vow
    return len(vow & set(str)), len(con & set(str))

str = input()
cyc, tim = tm.Timer('count(str)', globals = globals()).autorange()
print(cyc * 1 / tim)

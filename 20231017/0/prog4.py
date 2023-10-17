import timeit as tm
from collections import Counter

def dictionary(text) :
    dict = {}
    for i in text :
        if i in dict.keys() :
            dict[i] += 1
        else :
            dict[i] = 1
    return dict

count_dict = lambda text : Counter(text)

text = input().split()
print(tm.Timer('dictionary(text)', globals = globals()).autorange())
print(tm.Timer('count_dict(text)', globals = globals()).autorange())

import types

class dump(type):
    def wrapper(val, name):
        def little_wrapper(self, *args, **kwargs):
            arr1 = []
            for i in args:
                if isinstance(i, (str, int, float, bool)):
                    arr1.append(i)
            arr1 = tuple(arr1)
            dict2 = {}
            for i in kwargs.keys():
                if isinstance(kwargs[i], (str, int, float, bool)):
                    dict2[i] = kwargs[i]
            print("{}: {}, {}".format(name, arr1, dict2))
            return val(self, *args, **kwargs)
        return little_wrapper
    
    def __new__(cls, name, base, dict):
        for i in dict.keys():
            if isinstance(dict[i], types.FunctionType):
                dict[i] = cls.wrapper(dict[i], i)
        return super().__new__(cls, name, base, dict)
    

import sys
exec(sys.stdin.read())
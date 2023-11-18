class Alpha:
    __slots__ = tuple([chr(i) for i in range(ord('a'), ord('z') + 1)])

    def __init__(self, **kwargs):
        for i, val in kwargs.items():
            if i in Alpha.__slots__:
                setattr(self, i, val)
            else:
                raise AttributeError
    def __str__(self):
        res = []
        for i in Alpha.__slots__:
            if hasattr(self, i):
                res.append(f"{i}: {getattr(self, i)}")
        return ", ".join(res)

class AlphaQ:
    def __init__(self, **kwargs):
        for i, val in kwargs.items():
            if i in [chr(j) for j in range(ord('a'), ord('z') + 1)]:
                setattr(self, i, val)
            else:
                raise AttributeError
                                
    def __str__(self):
        res = []
        for i in [chr(j) for j in range(ord('a'), ord('z') + 1)]:
            if hasattr(self, i):
                res.append(f"{i}: {getattr(self, i)}")
        return ", ".join(res)
    
    def __setattr__(self, key, val):
        if key in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
            return super().__setattr__(key, val)
        else:
            raise AttributeError
                                                    
    def __getattr__(self, key):
        if key in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
            return super().__getattr__(key)
        else:
            raise AttributeError

import sys
exec(sys.stdin.read())


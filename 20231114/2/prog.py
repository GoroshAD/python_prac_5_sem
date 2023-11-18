class Num:
    def __init__(self):
        self.number = 0

    def __get__(self, obj, cls):
        try:
            return obj.number
        except:
            obj.number = 0
        return obj.number

    def __set__(self, obj, value):
        if hasattr(value, 'real'):
            obj.number = value.real
        else:
            obj.number = len(value)


import sys
exec(sys.stdin.read())

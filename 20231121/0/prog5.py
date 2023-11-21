import pickle
print(pickle.dumps("QWERTY"))
print(pickle.dumps("QWERTYt"))
print(pickle.dumps(["QWERTY", 100500]*8, protocol=0))

class C:
    def __init__(self, i):
        self.var = i

c = C(2)
print(c1:=pickle.dumps(c))
print(c2:=pickle.loads(c1))
print(c2.var)
del C
class C:
    def __init__(self, i):
        self.var = str(i*2)
#тупо даже не вызывал второй раз инит, а просто понапихал поля что уже были
print(c2.var)

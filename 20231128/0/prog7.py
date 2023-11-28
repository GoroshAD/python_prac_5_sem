import inspect
class C:
    ann: int
    def __init__(self, x):
        typ = inspect.get_annotations(self.__class__)["ann"]
        if not isinstance(x, typ):
            raise TypeError
        self.ann = x



class C :
    _var = 0

    @property
    def age(self) :
        if self._var == 42 :
            print("secret value!")
            return -1
        else :
            return self._var


    @age.setter
    def age(self, num) :
        if num <= 128 :
            self._var = num
        else :
            print("Too old!")
            raise ValueError

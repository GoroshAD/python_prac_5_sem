class Rectangle :
    rectcnt = 0

    def __abs__(self) :
        return abs((self.left[0] - self.right[0]) * (self.right[1] - self.left[1]))

    def __init__(self, x1, y1, x2, y2) :
        Rectangle.rectcnt += 1
        string = "rect_" + str(Rectangle.rectcnt)
        setattr(self, string, Rectangle.rectcnt)
        self.left, self.right = (x1, y1), (x2, y2)
        pass

    def __str__(self) :
        return "{}{}{}{} {}".format((self.left[0],self.left[1]),(self.left[0],self.right[1]),(self.right[0],self.right[1]),(self.right[0],self.left[1]), Rectangle.rectcnt)

    def __lt__(self, other) :
        return abs(self) > abs(other)

    def __eq__(self, other) :
        return abs(self) == abs(other)

    def __rt__(self, other) :
        return abs(self) < abs(other)

    def __le__(self, other) :
        return abs(self) >= abs(other)

    def __re__(self, other) :
        return abs(self) <= abs(other)

    def __mul__(self, i) :
        return Rectangle(self.left[0] * i, self.left[1] * i, self.right[0] * i, self.right[1] * i)

    def __rmul__(self, i) :
        return Rectangle(self.left[0] * i, self.left[1] * i, self.right[0] * i, self.right[1] * i)

    def __getitem__(self, index) :
        return [(self.left[0], self.left[1]), (self.left[0], self.right[1]), (self.right[0], self.right[1]), (self.right[0], self.left[1])][index]

    def __del__(self) :
        print(f"Deleting {self}")
        Rectangle.rectcnt -= 1
        pass



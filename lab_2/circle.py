from shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(x, y)
        self._radius = radius

    @property
    def radius(self):
        pass

    @radius.setter
    def radius(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

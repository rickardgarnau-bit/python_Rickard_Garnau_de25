from shape import Shape


class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)  # we reuse the attributes from the Shape class
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def move(self, dx, dy):

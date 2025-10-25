from shape import Shape


class Rectangle(Shape):
    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
        super().__init__(x, y)
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

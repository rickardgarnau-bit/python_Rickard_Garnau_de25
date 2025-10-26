from shape import Shape
import matplotlib as plt


class Rectangle(Shape):
    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * {self.width + self.height}

    def draw(self):
        rectangle = plt.Rectangle((0, 0), self.width, self.height)

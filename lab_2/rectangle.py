from shape import Shape


class Rectangle(Shape):
    # The constructor of the Rectangle class initializes the recangle object
    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
        super().__init__(x, y)  # we reuse the attributes from the Shape class
        self._width = width
        self._height = height

    @property
    def width(self):
        pass

    @width.setter
    def width(self):
        pass

    @property
    def height(self):
        pass

    @height.setter
    def height(self):
        pass

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

from shape import Shape


class Rectangle(Shape):
    # The constructor of the Rectangle class initializes the recangle object
    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
        super().__init__(x, y)  # we reuse the attributes from the Shape class
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("The width has to be number")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("The height has to be number")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    def __repr__(self):
        return f"Rectangle(width={self._width}, height={self._height}, area={self.area}, perimeter={self.perimeter}))"

    def __str__(self):
        return f"The area of the rectangle is: {self.area}. The perimeter of the rectangle is: {self.perimeter}"


r = Rectangle(width=4, height=6)

print(f"Width: {r.width}")
print(f"Height: {r.height}")
print(f"Area: {r.area}")
print(f"Perimeter: {r.perimeter}")

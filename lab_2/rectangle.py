from shape import Shape


class Rectangle(Shape):
    # The constructor of the Rectangle class initializes the recangle object
    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
        super().__init__(x, y)  # we reuse the attributes from the Shape class
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("The width has to be number")
        self._value = self._width

    @property
    def height(self):
        pass

    @height.setter
    def height(self, value):
         if not isinstance(value, (int, float)):
            raise TypeError("The height has to be number")
        self._value = self._height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def __eq__(self, other):



rectangle = Rectangle(width=5, height=5)

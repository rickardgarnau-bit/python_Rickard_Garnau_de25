from shape import Shape  # Import the "Shape" template from our shape.py file
import math  # Needed for math.isclose


# Our new Rectangle class, which inherits all features from Shape
class Rectangle(Shape):
    """
    Represents a Rectangle shape inheriting from Shape.

    Attributes:
        x (float): The x-coordinate of the top-left corner.
        y (float): The y-coordinate of the top-left corner.
        width (float): The width of the rectangle (must be non-negative).
        height (float): The height of the rectangle (must be non-negative).
    """

    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
        """Call the parent class constructor to save x and y."""
        super().__init__(x, y)
        # Set the width and height. This will call our setters below.
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self._width * self._height

    @property
    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

    @property
    def is_square(self) -> bool:
        """
        Checks if the rectangle is a square (width and height are equal).
        Uses math.isclose() for safe float comparison.
        """
        return math.isclose(self._width, self._height)

    @property
    def width(self) -> float:
        """Gets or the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value: float):
        """Sets the width, ensuring it's a non-negative number."""
        if not isinstance(value, (int, float)):
            raise TypeError("The width has to be a number")
        if value < 0:
            raise ValueError("The width cannot be negative")
        self._width = float(value)

    @property
    def height(self) -> float:
        """Gets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("The height has to be a number")
        if value < 0:
            raise ValueError("The height cannot be negative")
        self._height = float(value)

    def __repr__(self) -> str:
        """Returns the formal string representation of the Rectangle."""
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __str__(self) -> str:
        """Returns the user-friendly string representation of the Rectangle."""
        return (
            f"Rectangle (w={self.width}, h={self.height}) at ({self.x}, {self.y}). "
            f"Area: {self.area:.2f}, Perimeter: {self.perimeter:.2f}"
        )


"""This test code below only runs when we execute this file directly"""
if __name__ == "__main__":

    """Create an instance of the class Rectangle"""
    r = Rectangle(width=4, height=6)

    """Use our properties to print information with formating"""
    print(f"Width: {r.width}")
    print(f"Height: {r.height}")
    print(f"Area: {r.area:.2f}")
    print(f"Perimeter: {r.perimeter:.2f}")
    print(f"Is it a square? {r.is_square}")

    print(r)
    print(repr(r))

    r2 = Rectangle(width=5, height=5)
    print(f"\nIs r2 a square? {r2.is_square}")

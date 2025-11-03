from shape import Shape
import math


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
        """Gets the width of the rectangle."""
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
        """Sets the height, ensuring it's a non-negative number."""
        if not isinstance(value, (int, float)):
            raise TypeError("The height has to be a number")
        if value < 0:
            raise ValueError("The height cannot be negative")
        self._height = float(value)

    def __repr__(self) -> str:
        """Returns the formal string representation of the Rectangle."""
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __str__(self) -> str:
        return f"Rectangle (w={self.width}, h={self.height}) at ({self.x}, {self.y}). Area: {self.area:.2f}, Perimeter: {self.perimeter:.2f}"


if __name__ == "__main__":
    # Create an instance of the class Rectangle
    r = Rectangle(width=4, height=6)

    # Use our properties to print information with formatting
    print(f"Width: {r.width}")
    print(f"Height: {r.height}")
    print(f"Area: {r.area:.2f}")
    print(f"Perimeter: {r.perimeter:.2f}")
    print(f"Is it a square? {r.is_square}")

    print(r)
    print(repr(r))

    r2 = Rectangle(width=5, height=5)
    print(f"\nIs r2 a square? {r2.is_square}")

    print(f"\nOld position of r: ({r.x}, {r.y})")
    r.translate(10, 5)
    print(f"New position of r: ({r.x}, {r.y})")
    r.translate(-3, 0)
    print(f"New position of r: ({r.x}, {r.y})")

circle1 = plt.Circle((0, 0), 0.2, color="r")
plt.gca().add_patch(circle1)

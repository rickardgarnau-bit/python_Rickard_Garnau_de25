from shape import Shape
import math


class Circle(Shape):
    """
    Represents a Circle shape inheriting from Shape.

    Attributes:
        x (float): The x-coordinate of the circle's center.
        y (float): The y-coordinate of the circle's center.
        radius (float): The radius of the circle.
    """

    def __init__(self, x=0, y=0, radius=1):
        """Initializes a new Circle instance."""
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self) -> float:
        """Gets or the radius of the circle."""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """Sets the radius, ensuring it's a non-negative number."""
        if not isinstance(value, (int, float)):
            raise TypeError("The radius has to be of type(int, float)")
        if value < 0:
            raise ValueError("The radius cannot be negative")
        self._radius = float(value)

    @property
    def area(self) -> float:
        return math.pi * self._radius**2

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def is_unit_circle(self) -> bool:
        return (
            math.isclose(self.radius, 1)
            and math.isclose(self.x, 0)
            and math.isclose(self.y, 0)
        )

    """ source from https://www.w3schools.com/python/ref_math_isclose.asp and formatting from 'LLM' """

    def __repr__(self) -> str:
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self) -> str:
        return (
            f"Center circle ({self.x}, {self.y}) and radius {self.radius}. "
            f"Area: {self.area:.2f}, Perimeter: {self.perimeter:.2f}"
        )


if __name__ == "__main__":

    c = Circle(radius=5)

    print(f"Radius: {c.radius}")
    print(f"Area: {c.area:.2f}")
    print(f"Perimeter: {c.perimeter:.2f}")

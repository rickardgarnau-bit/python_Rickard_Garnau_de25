from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'x' must be a number, (int or float)")
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'y' must be a number, (int or float)")
        else:
            self._y = value

    @property
    @abstractmethod
    def area(self):
        """The abstract property for the area of the shape."""
        pass

    @property
    @abstractmethod
    def perimeter(self):
        """The abstract property for the perimeter of the shape."""
        pass

    def __eq__(self, other):
        if not isinstance(other, Shape):
            return False
        return self.area == other.area and self.perimeter == other.perimeter

    def __lt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented  # Allows Python to try other > self
        return self.area < other.area

    def __le__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area <= other.area

    def __gt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area > other.area

    def __ge__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area >= other.area

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __str__(self):
        return f"Shape at position ({self.x}, {self.y})"

    def translate(self, dx, dy):
        """Moves the shape by dx and dy."""
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("Translate values must be numbers (int or float)")

        self.x += dx
        self.y += dy

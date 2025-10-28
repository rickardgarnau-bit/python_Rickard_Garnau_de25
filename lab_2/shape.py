from abc import ABC, abstractmethod


class Shape(ABC):  # The parent class Shape

    def __init__(self, x: float = 0, y: float = 0):  # Initalizing coordinates x and y
        self.x = x
        self.y = y

    @property  # getter for x
    def x(self):
        return self._x

    @x.setter  # setter for x with typecheck
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'x' must be a number, (int or float)")
        else:
            self._x = value

    @property  # getter for y
    def y(self):
        return self._y

    @y.setter  # setter for y with typecheck
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'y' must be a number, (int or float)")
        else:
            self._y = value

    @property
    @abstractmethod
    def area(self):
        pass

    # @abstractmethod to signal the subclasses that these methods are required else they will get a TypeError

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def __eq__(self, other):  # comparison operator - equal
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):  # less than, checks x then y
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __le__(self, other):  # less than or equal to
        if self.x == other.x:
            return self.y <= other.y
        return self.x < other.x

    def __gt__(self, other):  # greater than
        if self.x == other.x:
            return self.y > other.y
        return self.x > other.x

    def __ge__(self, other):  # greater or equal to
        if self.x == other.x:
            return self.y >= other.y
        return self.x > other.x

    # I got help and inspiration for the overloading comparison operators from:
    # https://docs.python.org/3/reference/datamodel.html#special-method-names

    def __repr__(
        self,
    ):  # formal representation for reviewing the object. https://www.geeksforgeeks.org/python/python-program-to-get-the-class-name-of-an-instance/
        return f"{self.__class__.__name__}, (x={self.x}, y={self.y})"

    def __str__(self):  # clean representation for viewing
        return f"Shape at position ({self.x}, {self.y})"

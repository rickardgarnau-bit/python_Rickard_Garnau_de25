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
            self._x = value  # If the check passes, save the value.

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

    # We don't know how to calculate the area or perimeter of a 'Shape',
    # so we leave it empty with 'pass' as a placeholder.

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, Shape):
            return False
        return self.area == other.area and self.perimeter == other.perimeter

    def __lt__(self, other):  # Less than
        if not isinstance(other, Shape):
            return NotImplemented  # https://docs.python.org/3/reference/datamodel.html
        return self.area < other.area

    def __le__(self, other):  # Less than or equal to
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area <= other.area

    def __gt__(self, other):  # Greater than
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area > other.area

    def __ge__(self, other):  # Greater or equal to
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area >= other.area

    # I got help and inspiration for the overloading comparison operators from:
    # https://docs.python.org/3/reference/datamodel.html#special-method-names

    # self.__class__.__name__ is a clever way to get the *actual* class name,
    # instead of just "Shape". Used by developers review the code, debug.
    # https://www.geeksforgeeks.org/python/python-program-to-get-the-class-name-of-an-instance/
    def __repr__(self):
        return f"{self.__class__.__name__}, (x={self.x}, y={self.y})"

    def __str__(self):  # clean representation for viewers
        return f"Shape at position ({self.x}, {self.y})"

    def translate(self, dx, dy):  # a method to move the shape around.
        # check if the values are numeric before moving
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("Translate values must be numbers (int or float)")
        # if numeric add to x an y.
        self.x += dx
        self.y += dy

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
            raise TypeError
        else:
            self._x = value

    @property  # getter for y
    def y(self):
        return self._y

    @y.setter  # setter for y with typecheck
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        else:
            self._y = value

    @property
    @abstractmethod
    def area(self):
        pass

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
    # https://www.programiz.com/python-programming/operator-overloading

    def __repr__(self):  # formal representation for reviewing the object
        pass

    def __str__(self):  # clean representation for viewing
        pass

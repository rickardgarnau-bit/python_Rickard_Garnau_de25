from abc import ABC, abstractmethod


class Shape(ABC):  # The parent class Shape
    """The constructor of the Shape class initializes and stores the attributes
    the other shapes will use"""

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
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

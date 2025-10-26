from abc import ABC, abstractmethod


class Shape(ABC):  # The parent class Shape
    """The constructor of the Shape class initializes and stores the attributes
    the other shapes will use"""

    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0 or value > 100:
            raise ValueError("Negative numbers or numbers over hundred are not allowed")
        else:
            self._value = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0 or value > 100:
            raise ValueError("Negative numbers or numbers over hundred are not allowed")

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

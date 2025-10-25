from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    @property
    @abstractmethod
    def area():
        pass

    @property
    @abstractmethod
    def perimeter():
        pass

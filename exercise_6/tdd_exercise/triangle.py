import numbers


class Triangle:
    # x and y optional
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if not isinstance(value, numbers.Number):
            raise ValueError("must be a number")

        if value <= 0:
            raise ValueError("base must be larger than zero")
        self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, bool) or not isinstance(value, numbers.Number):
            raise ValueError("height must be a numeric value")
        if value <= 0:
            raise ValueError("height must be larger than zero")
        self._height = value

    @property
    def area(self):
        return 0.5 * self.base * self.height

    # @property
    # def perimeter(self):
    #     pass

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            return NotImplemented
        return self.area == other.area

    def __lt__(self, other):
        if not isinstance(other, Triangle):
            return NotImplemented
        return self.area < other.area

    def __gt__(self, other):
        if not isinstance(other, Triangle):
            return NotImplemented
        return self.area > other.area

    def __repr__(self):
        return f"Triangle(Base= {self.base}, Height= {self.height}, Area= {self.area}"

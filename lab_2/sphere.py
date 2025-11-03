from utils import validate_number
import math


class Sphere:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        validate_number(value)
        if isinstance(value, bool):
            raise TypeError("Radius must not be a boolean value")
        if value <= 0:
            raise ValueError("Radius must be larger than zero")
        self._radius = value

    @property
    def surface_area(self):
        return 4 * math.pi * (self.radius**2)

    @property
    def volume(self):
        return (4 / 3) * math.pi * (self.radius**3)

    @property
    def circumference(self):
        """Calculates the circumference of the great circle."""
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    try:
        r = float(input("Please enter the radius of the sphere: "))

        s = Sphere(r)

        print("The volume of the sphere is:", s.volume)
        print("The surface area of the sphere is:", s.surface_area)

    except (ValueError, TypeError) as e:
        print("Error:", e)

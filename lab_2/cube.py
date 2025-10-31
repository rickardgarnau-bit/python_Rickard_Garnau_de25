from utils import validate_number


class Cube:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        validate_number(value)
        if isinstance(value, bool):
            raise TypeError("Side must not be a boolean value")
        if value <= 0:
            raise ValueError("Side must be larger than zero")
        self._side = value

    def volume(self):
        """Return the volume of the cube."""
        return self.side**3

    def surface_area(self):
        """Return the surface area of the cube."""
        return 6 * (self.side**2)

    def perimeter(self):
        """Return the total edge length (perimeter) of the cube."""
        return 12 * self.side


if __name__ == "__main__":
    try:
        s = float(input("Please enter the side length of the cube: "))
        c = Cube(s)
        print("The volume of the cube is:", c.volume())
        print("The surface area of the cube is:", c.surface_area())
    except (ValueError, TypeError) as e:
        print("Error:", e)

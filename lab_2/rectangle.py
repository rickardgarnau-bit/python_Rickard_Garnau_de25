from shape import Shape  # Import the "Shape" template from our shape.py file


# Our new Rectangle class, which inherits all features from Shape
class Rectangle(Shape):
    # This method runs every time we create a new Rectangle object
    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
        # Call the parent class constructor to save x and y
        super().__init__(x, y)
        # Set the width and height. This will call our setters below.
        self.width = width
        self.height = height

    @property  # A "property" lets us call this method without parentheses (e.g., r.area)
    def area(self):
        # Calculate the area. Uses _width and _height to get the saved values.
        return self._width * self._height

    @property
    def perimeter(self):
        # Calculate the perimeter
        return 2 * (self._width + self._height)

    @property
    def is_square(self):
        # A property to check if the rectangle is actually a square
        return self._width == self._height  # Returns True if they are equal, else False

    @property
    def width(self):  # Getter lets us *get* the value (e.g., r.width)
        return self._width  # Returns the private value we stored

    @width.setter  # Setter runs when we set a value (e.g., r.width = 10)
    def width(self, value):
        if not isinstance(value, (int, float)):  # Check if the new value is a number
            raise TypeError("The width has to be number")  # If not, raise an error
        if value < 0:  # Also check that the value is not negative
            raise ValueError("The width cannot be negative")  # If it is, raise an error
        self._width = (
            value  # If all checks pass, save the value to the private _width variable
        )

    @property
    def height(self):  # Getter for height
        return self._height

    @height.setter
    def height(self, value):  # Setter for height
        if not isinstance(value, (int, float)):  # Same checks as for width
            raise TypeError("The height has to be number")
        if value < 0:
            raise ValueError("The height cannot be negative")
        self._height = value

    def __repr__(self):
        # The formal string for developers. Should look like the code to create the object.
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __str__(self):
        # The more readable string used when you run print.
        return f"The area of the rectangle is: {self.area}. The perimeter of the rectangle is: {self.perimeter}"

    def find_center(self):
        # A method to find the center point of the rectangle
        # The center = start (x, y) + half the width/height
        # This method comes from https://greenteapress.com/thinkpython/html/thinkpython016.html part 15.4
        center_x = self.x + self._width / 2.0
        center_y = self.y + self._height / 2.0
        return (center_x, center_y)  # Returns the center as a tuple, e.g., (10, 15)


# This test code below only runs when we execute this file directly (e.g., by typing "python rectangle.py" in the terminal)

# Create an instance of the class Rectangle.
r = Rectangle(width=4, height=6)

# Use our properties to print information
print(f"Width: {r.width}")
print(f"Height: {r.height}")
print(f"Area: {r.area}")
print(f"Perimeter: {r.perimeter}")
print(f"Is it a square? {r.is_square}")  # Should be False

# Create another rectangle, this one is a square. Idea from 'LLM'
r2 = Rectangle(width=5, height=5)
print(f"Is r2 a square? {r2.is_square}")  # Should be True

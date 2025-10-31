# Lab 2 - Geometry OOP

A Python project implementing geometric shapes using Object-Oriented Programming principles with inheritance and polymorphism.

## Project Overview

This project creates a hierarchy of geometric shapes with the following features:
- Abstract base class `Shape` with common functionality
- `Circle` and `Rectangle` classes inheriting from `Shape`
- Properties for area and perimeter calculations
- Operator overloading for comparisons
- Translation methods for moving shapes
- Error handling and validation

## UML Diagram

![UML Class Diagram](https://github.com/rickardgarnau-bit/python_Rickard_Garnau_de25/blob/main/lab_2/Uml_lab2.png)

*The UML diagram shows the class hierarchy with Shape as the abstract parent class and Circle and Rectangle as child classes.*

## Class Structure

### Shape (Abstract Base Class)
- **Attributes**: `x`, `y` (position coordinates)
- **Abstract Properties**: `area`, `perimeter`
- **Methods**: 
  - `translate(dx, dy)` - moves the shape
  - Comparison operators (`==`, `<`, `>`, `<=`, `>=`)
  - `__repr__()` and `__str__()` for string representation

### Rectangle
- **Additional Attributes**: `width`, `height`
- **Properties**: 
  - `area` - calculates width × height
  - `perimeter` - calculates 2(width + height)
  - `is_square` - checks if width equals height
- **Validation**: Ensures width and height are non-negative numbers

### Circle
- **Additional Attributes**: `radius`
- **Properties**:
  - `area` - calculates π × radius²
  - `perimeter` - calculates 2π × radius
  - `is_unit_circle` - checks if radius=1 and center at (0,0)
- **Validation**: Ensures radius is a non-negative number

### Running the code
```python
from circle import Circle
from rectangle import Rectangle

# Create shapes
circle1 = Circle(x=0, y=0, radius=1)  # unit circle
rectangle = Rectangle(x=0, y=0, width=5, height=3)

# Compare shapes
print(circle1 == rectangle)  # False

# Move shapes
circle1.translate(5, 3)
print(f"New position: ({circle1.x}, {circle1.y})")

# Check properties
print(f"Circle area: {circle1.area:.2f}")
print(f"Is square? {rectangle.is_square}")
```

## Code Examples

### Creating and comparing shapes
```python
circle1 = Circle(radius=5)
circle2 = Circle(radius=3)

print(circle1 > circle2)  # True (larger area)
print(circle1.area)       # 78.54
```

### Error handling
```python
try:
    circle = Circle(radius=-5)  # ValueError
except ValueError as e:
    print(e)  # "The radius cannot be negative"

try:
    rectangle = Rectangle(width="5", height=3)  # TypeError
except TypeError as e:
    print(e)  # "The width has to be a number"
```

## Design Decisions

### Inheritance
I chose to use an abstract base class (`Shape`) to enforce a common interface for all geometric shapes. This ensures that all shapes must implement `area` and `perimeter` properties.

### Comparison Logic
Shapes are compared based on both area and perimeter:
- Two shapes are equal (`==`) only if both area and perimeter match
- For `<` and `>`, area is compared first, perimeter is used as a tiebreaker
- This ensures consistent and logical sorting behavior

### Validation Strategy
All numeric inputs are validated using property setters to ensure:
- Type checking (must be int or float)
- Value checking (dimensions cannot be negative)
- This validation happens both during initialization and when modifying properties

### Float Comparison
I use `math.isclose()` for comparing floating-point numbers (e.g., in `is_square` and `is_unit_circle`) to avoid precision errors common with direct float comparisons.

## Sources and References

### Learning Resources
- **Python ABC Module**: [Python Official Documentation](https://docs.python.org/3/library/abc.html)
- **math.isclose()**: [W3Schools Reference](https://www.w3schools.com/python/ref_math_isclose.asp) - Used for safe float comparison in `is_unit_circle` and `is_square` methods
- **Property Decorators**: [Real Python - Python Property](https://realpython.com/python-property/)
- **Operator Overloading**: [Python Documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names)

### LLM Usage
I used Claude (Anthropic's AI assistant) for:
- **Code review and feedback** - Getting suggestions on best practices and potential improvements
- **Debugging help** - Understanding why validation wasn't working in `__init__` method
- **Documentation guidance** - Structuring this README and understanding docstring conventions
- **Python conventions** - Learning about `NotImplemented` vs `False` in comparison operators

All core logic and implementation was written by me. The LLM was used as a learning tool and code reviewer.

## Testing

Manual tests are included in each file under `if __name__ == "__main__":` blocks. Run them with:
```bash
python rectangle.py
python circle.py
```

Example test output:
```
Width: 4
Height: 6
Area: 24.00
Perimeter: 20.00
Is it a square? False
```

## Project Structure
```
geometry-oop/
├── README.md
├── shape.py          # Abstract base class
├── rectangle.py      # Rectangle implementation
├── circle.py         # Circle implementation
└── uml_diagram.png   # UML class diagram
```

## Future Improvements
- Add 3D shapes (Cube, Sphere)
- Implement unit tests with pytest
- Add visualization with matplotlib
- Create a ShapePlotter class for drawing multiple shapes

## Student
Rickard Garnau  
Lab 2 - Geometry OOP

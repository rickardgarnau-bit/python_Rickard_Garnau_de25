import matplotlib.pyplot as plt
import matplotlib.patches as patches

from shape import Shape
from rectangle import Rectangle
from circle import Circle


class Shape2DPlotter:
    """
    A class to plot 2D shapes that inherit from Shape.
    This class handles all Matplotlib-related logic.
    """

    def __init__(self, title="My 2D Shapes"):
        """Create the drawing area (canvas) ONCE in the constructor"""
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.ax.set_aspect("equal")  # Ensures circles are round.
        self.ax.grid(True)
        self.ax.set_title(title)
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")

    def add_shape(self, shape_obj: Shape):
        """
        Adds a shape object (like Circle or Rectangle) to the plot.
        """

        if isinstance(shape_obj, Circle):
            """Translate" Circle object into a Matplotlib patch"""
            patch = patches.Circle(
                (shape_obj.x, shape_obj.y),  # Center coordinates
                shape_obj.radius,
                facecolor="blue",
                alpha=0.6,
            )
            self.ax.add_patch(patch)

        elif isinstance(shape_obj, Rectangle):
            patch = patches.Rectangle(
                (shape_obj.x, shape_obj.y),  # Bottom-left corner
                shape_obj.width,
                shape_obj.height,
                facecolor="red",
                alpha=0.6,
            )
            self.ax.add_patch(patch)

        else:
            print(f"Warning: Cannot draw unknown shape type {type(shape_obj)}")

    def show_plot(self):
        """
        Displays the final plot with all added shapes.
        """

        """Rescale the axes and show the plot"""
        self.ax.relim()  # Recalculate limits
        self.ax.autoscale_view()  # Rescale the view
        plt.show()


if __name__ == "__main__":

    print("Creating plotter and shapes...")

    # Create one plotter
    my_plotter = Shape2DPlotter(title="Test Plot of My Shapes")

    # Create custom shape objects
    c1 = Circle(x=5, y=5, radius=4)
    r1 = Rectangle(x=0, y=0, width=3, height=6)
    c2 = Circle(x=-3, y=-2, radius=1.5)
    r2 = Rectangle(x=-8, y=2, width=2, height=2)  # A square

    # Add all shapes to the plotter
    my_plotter.add_shape(c1)
    my_plotter.add_shape(r1)
    my_plotter.add_shape(c2)
    my_plotter.add_shape(r2)

    print("Showing plot...")
    my_plotter.show_plot()

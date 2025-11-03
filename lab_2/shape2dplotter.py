import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle, Circle


"""Create a Figure and a set of Axes."""

fig, ax = plt.subplots()


""" Define the Rectangle patch
    We define its bottom-left corner (0.2, 0.2), width, height, and colors."""

rect = Rectangle(
    (0.2, 0.2), width=0.5, height=0.3, edgecolor="blue", facecolor="lightblue"
)

""" Define the Circle patch

    We define its center (0.5, 0.5), radius, and colors."""

circle = Circle((0.5, 0.5), radius=0.2, edgecolor="red", facecolor="lightcoral")


""" Add both patches to the Axes."""

ax.add_patch(rect)

ax.add_patch(circle)


""" Configure the plot's appearance

    Set the visible boundaries for the x-axis (0 to 1)."""

ax.set_xlim(0, 1)

""" Set the visible boundaries for the y-axis (0 to 1)."""

ax.set_ylim(0, 1)

""" Set the aspect ratio to 'equal' to ensure the circle is not oval-shaped."""

ax.set_aspect("equal")

""" Add a background grid for easier viewing."""

plt.grid(True)

"""Set the main title of the plot."""

plt.title("Rectangle and Circle")


"""Display the final plot."""

plt.show()

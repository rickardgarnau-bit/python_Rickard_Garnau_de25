import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

fig, ax = plt.subplots()

rect = Rectangle(
    (0.2, 0.2), width=0.5, height=0.3, edgecolor="blue", facecolor="lightblue"
)

circle = Circle((0.5, 0.5), radius=0.2, edgecolor="red", facecolor="lightred")

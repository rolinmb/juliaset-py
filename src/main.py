import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Mandelbrot set parameters
width, height = 800, 800  # Resolution
max_iter = 300  # Maximum number of iterations

# Set the initial bounds of the plot
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5

# Function to compute the Mandelbrot Set
def mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros(C.shape, dtype=complex)
    div_time = np.zeros(C.shape, dtype=int)
    mask = np.ones(C.shape, dtype=bool)

    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + C[mask]
        mask = (np.abs(Z) <= 2)
        div_time[~mask & (div_time == 0)] = i

    return div_time

# Set up the figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.axis("off")
im = ax.imshow(np.zeros((height, width)), extent=(x_min, x_max, y_min, y_max), cmap="inferno")

# Animation function
def animate(frame):
    zoom_factor = 0.95**frame
    x_center, y_center = -0.75, 0.0  # Center of zoom
    x_width = (x_max - x_min) * zoom_factor
    y_height = (y_max - y_min) * zoom_factor
    x_min_new, x_max_new = x_center - x_width / 2, x_center + x_width / 2
    y_min_new, y_max_new = y_center - y_height / 2, y_center + y_height / 2

    mandelbrot_set = mandelbrot(x_min_new, x_max_new, y_min_new, y_max_new, width, height, max_iter)
    im.set_data(mandelbrot_set)
    im.set_extent((x_min_new, x_max_new, y_min_new, y_max_new))
    return [im]

# Create the animation
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()

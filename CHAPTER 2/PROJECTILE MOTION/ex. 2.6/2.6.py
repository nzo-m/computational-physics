import numpy as np
from nzo import plot

v0 = 700
g = 9.8
angles = [30, 35, 40, 45, 50, 55]
h = 0.1
tf = 150

xs = []
ys = []
labels = []

for angle in angles:
    theta = np.radians(angle)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    ti = np.arange(0, tf + h, h)
    xi = np.zeros_like(ti)
    yi = np.zeros_like(ti)

    for n in range(len(ti) - 1):
        xi[n + 1] = xi[n] + h * vx
        vy -= g * h
        yi[n + 1] = yi[n] + h * vy
        if yi[n + 1] < 0:
            xi = xi[:n + 2]
            yi = yi[:n + 2]
            break

    xs.append(xi / 1000)
    ys.append(yi / 1000)
    labels.append(f"{angle}°")

plot(
    *sum(zip(xs, ys), ()),
    title="Euler Trajectories (No Air Resistance)",
    xlabel="Horizontal Distance x (km)",
    ylabel="Vertical Height y (km)",
    labels=labels)

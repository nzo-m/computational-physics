import numpy as np
from nzo import plot

g = 9.8
v0 = 700
p0 = 1.225
B2ref = 4e-5
y0 = 1.0e4
a = 6.5e-3
T = 300
alpha = 2.5
dt = 0.1
tmax = 300
angles = [30, 45]
temperatures = [270, 330]

def p_adiabatic(y):
    return p0 * (1 - a * y / T) ** alpha

def approx_temp(angle_deg, T0):
    B2 = B2ref * (T0 / T) ** alpha

    theta = np.radians(angle_deg)
    vx, vy = v0 * np.cos(theta), v0 * np.sin(theta)
    x, y = 0, 0

    xs, ys = [x], [y]
    t = 0

    while t < tmax and y >= 0:
        v = np.sqrt(vx**2 + vy**2)
        p = p_adiabatic(y)
        ax = -B2 * p * v * vx
        ay = -g - B2 * p * v * vy
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        xs.append(x)
        ys.append(y)
        t += dt

    return xs, ys

trajectories = []
labels = []

for T0 in temperatures:
    for angle in angles:
        xs, ys = approx_temp(angle, T0)
        trajectories.append((xs, ys))
        labels.append(f"{angle}° T={T0}K")

plotprep = []
for xs, ys in trajectories:
    plotprep.extend([xs, ys])

plot(
    *plotprep,
    labels=labels,
    title="Cannon Shell Trajectories: Winter vs Summer",
    xlabel="Distance (km)",
    ylabel="Height (km)",
)

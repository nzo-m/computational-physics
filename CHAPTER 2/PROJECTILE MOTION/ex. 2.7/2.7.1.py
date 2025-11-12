import numpy as np
from nzo import plot

g = 9.8
v0 = 700
p0 = 1.225
B2 = 4e-5
y0 = 1.0e4
a = 6.5e-3
T0 = 300
alpha = 2.5
dt = 0.1
tmax = 300
angles = [30, 45]

def p_isothermal(y):
    return p0 * np.exp(-y / y0)

def p_adiabatic(y):
    return p0 * (1 - a * y / T0) ** alpha

def approx(angleshoot, iso_or_adi):
    theta = np.radians(angleshoot)
    vx, vy = v0 * np.cos(theta), v0 * np.sin(theta)
    x, y = 0, 0

    xs, ys = [x], [y]
    t = 0

    while t < tmax and y >= 0:
        v = np.sqrt(vx**2 + vy**2)
        p = iso_or_adi(y)
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

for angle in angles:
    xs_iso, ys_iso = approx(angle, p_isothermal)
    xs_adi, ys_adi = approx(angle, p_adiabatic)

    trajectories.append((xs_iso, ys_iso))
    trajectories.append((xs_adi, ys_adi))

    labels.append(f"{angle}° Isothermal")
    labels.append(f"{angle}° Adiabatic")


plotprep = []
for xs, ys in trajectories:
    plotprep.extend([xs, ys])

plot(
    *plotprep,
    labels=labels,
    title="Cannon Shell Trajectories",
    xlabel="Distance (km)",
    ylabel="Height (km)",
)

import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'grid', 'bright'])
plt.figure(figsize=(12, 8))

g = 9.8
v0 = 700
p0 = 1.225
B2 = 4e-5
a = 6.5e-3
T0 = 300.0
alpha = 2.5
dt = 0.1
tmax = 300

def pAir(y):
    return p0 * (1 - a * y / T0) ** alpha

def test(angle):
    theta = np.radians(angle)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)
    x = 0
    y = 0
    xs = [0]
    ys = [0]
    t = 0

    while t < tmax and y >= 0:

        v = np.sqrt(vx*vx + vy*vy)
        rho = pAir(y)
        ax = -B2 * rho * v * vx
        ay = -g - B2 * rho * v * vy
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        xs.append(x)
        ys.append(y)

        t += dt

    return np.array(xs), np.array(ys)

def no_density(angle):
    theta = np.radians(angle)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)
    x = 0
    y = 0
    xs = [0]
    ys = [0]
    t = 0

    while t < tmax and y >= 0:
        v = np.sqrt(vx*vx + vy*vy)
        rho = p0
        ax = -B2 * rho * v * vx
        ay = -g - B2 * rho * v * vy
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        xs.append(x)
        ys.append(y)
        t += dt

    return np.array(xs), np.array(ys)

angles = np.arange(10, 80, 1)
ranges = []

for ang in angles:
    xs, ys = test(ang)
    ranges.append(xs[-1])

ranges = np.array(ranges)

angMaxRange = angles[np.argmax(ranges)]
maxrange = np.max(ranges) / 1000

print(f"Max range = {maxrange:.2f} km at angle = {angMaxRange}°")

for ang in [35, 45, angMaxRange]:
    xs, ys = test(ang)
    plt.plot(xs/1000, ys/1000, lw=2,
             label=f"{ang}° (with density)")
    xs2, ys2 = no_density(ang)
    plt.plot(xs2/1000, ys2/1000, lw=2, linestyle="--",
             label=f"{ang}° (no density)")

plt.xlabel("Distance (km)")
plt.ylabel("Height (km)")
plt.title(f"With vs Without Density Correction\nMax Range at {angMaxRange}°")
plt.legend()
plt.savefig("maxrange-comparison", dpi=300, bbox_inches='tight')
plt.show()

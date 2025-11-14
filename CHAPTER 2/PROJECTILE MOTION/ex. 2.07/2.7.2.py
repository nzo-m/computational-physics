import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science','grid','bright'])
plt.figure(figsize=(12,8))

g = 9.8
v0 = 700
p0 = 1.225
B2ref = 4e-5
y0 = 1.0e4
a = 6.5e-3
T_ref = 300
alpha = 2.5
dt = 0.1
tmax = 300

angles = [30, 45]
temperatures = [270, 330]

def pAdiabatic(y):
    return p0 * (1 - a * y / T_ref) ** alpha

def approx_temp(angle_deg, T0):
    B2 = B2ref * (T0 / T_ref) ** alpha

    theta = np.radians(angle_deg)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    x, y = 0, 0
    xs = [x]
    ys = [y]
    t = 0

    while t < tmax and y >= 0:
        v = np.sqrt(vx**2 + vy**2)
        p = pAdiabatic(y)

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

for angle in angles:
    for T0 in temperatures:
        xs, ys = approx_temp(angle, T0)

        if T0 == 270:
            style = '-'
        else:
            style = '--'

        plt.plot(
            np.array(xs)/1000,
            np.array(ys)/1000,
            linestyle=style,
            lw=2.5,
            label=f"{angle}°  T={T0}K"
        )

plt.xlabel("Distance (km)")
plt.ylabel("Height (km)")
plt.title("Trajectories: Winter vs. Summer")
plt.legend()
plt.savefig("winter270-vs-summer330", dpi=300, bbox_inches='tight')
plt.show()

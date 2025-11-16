import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'grid', 'bright'])

g = 9.8
p0 = 1.225
B2 = 4e-5
a = 6.5e-3
T0 = 300.0
alpha = 2.5
dt = 0.1
tmax = 300

def pAir(y):
    return p0 * (1 - a * y / T0) ** alpha

def hit(v0, angle, ytarget):
    theta = np.radians(angle)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)
    x = 0
    y = 0
    t = 0
    yprev = y
    xs = [x]
    ys = [y]

    while t < tmax and y >= -2000:
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

        if (yprev <= ytarget and y >= ytarget) or (yprev >= ytarget and y <= ytarget):
            return xs, ys, x, y

        yprev = y
        t += dt

    return xs, ys, None, None

def minv(ytarget, angle):
    v = 100
    vmax = 2000

    while v < vmax:
        xs, ys, xhit, yhit = hit(v, angle, ytarget)

        if xhit is not None:
            return v, xs, ys, xhit, yhit

        v += 5
    return None

targets = [-2000, -1000, 1000, 2000]
angles = [35, 45]

fig, axes = plt.subplots(len(angles), len(targets), figsize=(20, 10), sharex=True, sharey=True)

for i, angle in enumerate(angles):

    for j, yT in enumerate(targets):

        ax = axes[i, j]
        vmin, xs, ys, xhit, yhit = minv(yT, angle)

        if vmin is not None:
            ax.plot(np.array(xs)/1000, np.array(ys)/1000, lw=2, label=f"Minimun Velocity={vmin:.1f} m/s")
            ax.plot(xhit/1000, yhit/1000, 'o', markersize=5, label="Target")

        ax.set_title(f"Angle={angle}°, Target={yT/1000:.1f} km")
        ax.set_xlabel("Distance (km)")
        ax.set_ylabel("Height (km)")
        ax.legend()
        ax.grid(True)

plt.suptitle("Hittin Targets at Different Altitudes and Angles")
plt.savefig("hithit", dpi=300, bbox_inches='tight')
plt.show()

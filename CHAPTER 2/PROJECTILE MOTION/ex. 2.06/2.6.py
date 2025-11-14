import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science','grid','bright'])
plt.figure(figsize=(12,8))

g = 9.8
v0 = 700
dt = 0.01
angles = [30, 35, 40, 45, 50, 55]

for angle in angles:
    anglerad = np.radians(angle)
    vx = v0*np.cos(anglerad)
    vy = v0 * np.sin(anglerad)

    xs, ys = [0], [0]
    vycurrent = vy

    while ys[-1] >= 0:
        vycurrent = vycurrent - g*dt
        xs.append(xs[-1] + vx*dt)
        ys.append(ys[-1] + vycurrent*dt)

    tflight = 2 * vy / g
    ts = np.linspace(0, tflight, 500)
    xexact = vx * ts
    yexact = vy * ts - 0.5 * g * ts**2

    plt.plot(np.array(xs)/1000, np.array(ys)/1000, label=f"Euler {angle}°", lw=2)
    plt.plot(xexact/1000, yexact/1000, '--', label=f"Exact {angle}°", lw=2)

plt.xlabel("x (km)")
plt.ylabel("y (km)")
plt.title("Projectile Motion")
plt.legend()
plt.savefig("trajectories-no-air.png", dpi=300, bbox_inches='tight')
plt.show()

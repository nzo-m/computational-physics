import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'grid', 'bright'])
plt.figure(figsize=(12, 8))

g0 = 9.8
Re = 6.371e6
v0 = 700.0
rho0 = 1.225
B2 = 4e-5
a = 6.5e-3
T0 = 300.0
alpha = 2.5
dt = 0.1
tmax = 300.0
angle = 45

def rho_adiabatic(y):
    return (rho0 * (1 - a * y / T0) ** alpha)

def gy(y):
    return g0 * (Re / (Re + y)) ** 2

def simulate(angledeg, use_gy):
    theta = np.radians(angledeg)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    x, y= 0,0
    xs = [x]
    ys = [y]

    t = 0
    while t < tmax and y >= 0:
        v = np.sqrt(vx**2 + vy**2)
        rho = rho_adiabatic(y)

        if use_gy:
            g = gy(y)
        else:
            g = g0

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

g_x, g_y = simulate(angle, use_gy=False)
gy_x, gy_y = simulate(angle, use_gy=True)

range_g = g_x[-1] / 1000
range_gy = gy_x[-1] / 1000

difference = (range_g - range_gy) / range_g * 100

print(f"Constant g range: {range_g:.3f} km")
print(f"g(y) range: {range_gy:.3f} km")
print(f"Range difference: {difference:.2f}%")

plt.plot(g_x/1000, g_y/1000, '-', label="Constant g", lw=2)
plt.plot(gy_x/1000,   gy_y/1000, '--', label="Variable g(y)", lw=2)

plt.xlabel("Distance (km)")
plt.ylabel("Height (km)")
plt.title("g(y) Effect on Projectile Motion\n45° test")
plt.legend()
plt.savefig("g(y)-effect", dpi=300, bbox_inches='tight')
plt.show()

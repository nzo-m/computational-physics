import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science','grid','bright'])
plt.figure(figsize=(12,8))

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

def pIsothermal(y):
    return p0 * np.exp(-y / y0)

def pAdiabatic(y):
    return p0 * (1 - a * y / T0) ** alpha

def approx(angleshoot, p_IsoAdi):
    theta = np.radians(angleshoot)
    vx, vy = v0 * np.cos(theta), v0 * np.sin(theta)
    x, y = 0, 0

    xs, ys = [x], [y]
    t = 0

    while t < tmax and y >= 0:
        v = np.sqrt(vx**2 + vy**2)
        p = p_IsoAdi(y)
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

iso = []
adi = []

for angle in angles:
    xs_iso, ys_iso = approx(angle, pIsothermal)
    xs_adi, ys_adi = approx(angle, pAdiabatic)

    iso.append((xs_iso, ys_iso))
    adi.append((xs_adi, ys_adi))

for i, angle in enumerate(angles):
    xs_iso, ys_iso = iso[i]
    xs_adi, ys_adi = adi[i]

    plt.plot(np.array(xs_iso)/1000, np.array(ys_iso)/1000,
             '-', label=f'Isothermal {angle}°', lw=2)
    plt.plot(np.array(xs_adi)/1000, np.array(ys_adi)/1000,
             '--', label=f'Adiabatic {angle}°', lw=2)

plt.xlabel("Distance (km)")
plt.ylabel("Height (km)")
plt.title("Trajectories (Isothermal vs. Adiabatic)")
plt.legend()
plt.savefig("adi-vs-iso", dpi=300, bbox_inches='tight')
plt.show()

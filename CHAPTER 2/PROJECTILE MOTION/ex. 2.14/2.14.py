import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'grid', 'bright'])

g = 9.8
rho = 1.225
Cd = 0.3
A = np.pi * (0.037/2)**2
m = 0.145
k = 0.5*rho*Cd*A / m

v0mph = 110
v0 = v0mph * 0.44704

thetadeg = 35
theta = np.radians(thetadeg)

vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)
vz0 = 0

def simulate(Zwind=0):
    dt = 0.01
    x = y = z = 0.0
    vx, vy, vz = vx0, vy0, vz0

    X, Y, Z = [], [], []

    while y >= 0:
        vxrel = vx
        vyrel = vy
        vzrel = vz - Zwind

        vrel = np.sqrt(vxrel**2 + vyrel**2 + vzrel**2)

        ax = -k * vrel * vxrel
        ay = -g - k * vrel * vyrel
        az = -k * vrel * vzrel

        vx += ax * dt
        vy += ay * dt
        vz += az * dt

        x += vx * dt
        y += vy * dt
        z += vz * dt

        X.append(x)
        Y.append(y)
        Z.append(z)

    return np.array(X), np.array(Y), np.array(Z)

X0, Y0, Z0 = simulate(Zwind=0)
Xw, Yw, Zw = simulate(Zwind=10 * 0.45)


print(f"No wind landing: x={X0[-1]:.2f} m, z={Z0[-1]:.2f} m")
print(f"With wind:       x={Xw[-1]:.2f} m, z={Zw[-1]:.2f} m")

print("\nLanding point change:")
print(f"Δx = {Xw[-1] - X0[-1]:.2f} m (forward)")
print(f"Δz = {Zw[-1] - Z0[-1]:.2f} m (sideways)")

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

axs[0].plot(X0, Y0, label="No wind")
axs[0].plot(Xw, Yw, label="10 mph crosswind")
axs[0].set_title("Effect of Crosswind (x–y)")
axs[0].set_xlabel("Distance x (m)")
axs[0].set_ylabel("Height y (m)")
axs[0].legend()
axs[0].grid(True)

axs[1].plot(X0, Z0, label="No wind")
axs[1].plot(Xw, Zw, label="10 mph crosswind")
axs[1].set_title("Effect of Crosswind (x–z)")
axs[1].set_xlabel("Distance x (m)")
axs[1].set_ylabel("Drift z (m)")
axs[1].legend()
axs[1].grid(True)
axs[1].set_aspect('equal', adjustable='datalim')

plt.savefig("effect-crosswind", dpi=300, bbox_inches='tight')
plt.show()

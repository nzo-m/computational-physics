import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'grid', 'bright'])

dt = 0.001
tmax = 2
ts = np.arange(0, tmax + dt, dt)

a = 10
b = 0
N0 = 1

Nexp = np.zeros_like(ts)
Nexp[0] = N0

for i in range(len(ts)-1):
    dN = a * Nexp[i]
    Nexp[i+1] = Nexp[i] + dN * dt

Nexact = N0 * np.exp(a * ts)

a1 = 10
b1 = 3
N01 = 1

Nlog1 = np.zeros_like(ts)
Nlog1[0] = N01

for i in range(len(ts)-1):
    dN = a1 * Nlog1[i] - b1 * Nlog1[i]**2
    Nlog1[i+1] = Nlog1[i] + dN * dt

a2 = 10
b2 = 0.01
N02 = 1000

Nlog2 = np.zeros_like(ts)
Nlog2[0] = N02

for i in range(len(ts)-1):
    dN = a2 * Nlog2[i] - b2 * Nlog2[i]**2
    Nlog2[i+1] = Nlog2[i] + dN * dt

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("Population Growth")

ax = axes[0]
ax.plot(ts, Nexp, label="Euler Numerical")
ax.plot(ts, Nexact, '--', label="Exact")
ax.set_title("Exponential Growth (b=0)")
ax.set_xlabel("Time")
ax.set_ylabel("N(t)")
ax.legend()

ax = axes[1]
ax.plot(ts, Nlog1, label=f"a=10, b=3, N0={N01}")
ax.set_title("Logistic Growth (Small N)")
ax.set_xlabel("Time")
ax.set_ylabel("N(t)")
ax.legend()

ax = axes[2]
ax.plot(ts, Nlog2, label=f"a=10, b=0.01, N0={N02}")
ax.set_title("Logistic Growth (Large N)")
ax.set_xlabel("Time")
ax.set_ylabel("N(t)")
ax.legend()

fig.tight_layout()
fig.savefig("population_growth.png", dpi=300, bbox_inches='tight')
plt.show()

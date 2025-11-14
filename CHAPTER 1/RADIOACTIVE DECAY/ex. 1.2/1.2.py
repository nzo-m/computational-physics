import numpy as np
import matplotlib.pyplot as plt
import scienceplots

x0 = 0
t0 = 0
v = 40
dt = 0.1
tf = 10

xs = []
ts = []

while t0 <= tf:
    x0 = x0 + v*dt
    t0 += dt
    ts.append(t0)
    xs.append(x0)

texact = np.linspace(0, tf, 200)
xexact = v*texact

plt.style.use(['science', 'grid', 'bright'])
plt.figure(figsize=(6,4))
plt.plot(ts, xs, '-', label='Euler Approx.', lw=2)
plt.plot(texact, xexact, '--', label='Exact Solution', lw=2)
plt.xlabel("Time(s)")
plt.ylabel("Horizontal Motion x (m)")
plt.title("Horizontal Motion (Euler vs. Exact)")
plt.legend()
plt.savefig("horizontal-motion.png", dpi=300, bbox_inches='tight')
plt.show()
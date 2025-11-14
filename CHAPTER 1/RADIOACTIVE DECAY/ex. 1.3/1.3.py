import numpy as np
import matplotlib.pyplot as plt
import scienceplots

v0, t0 = 0, 0
a, b = 10, 1
dt = 0.1
tf = 10

ts = []
vs = []

while t0 <= tf:
    dvdt = a - b*v0
    v0 = v0 + dvdt*dt
    t0 += dt
    vs.append(v0)
    ts.append(t0)

plt.style.use(['science', 'grid', 'bright'])
plt.figure(figsize=(6,4))
plt.plot(ts, vs, '-', lw=2)
plt.xlabel("Time(s)")
plt.ylabel("Velocity (m/s)")
plt.title("Terminal Velocity")
plt.savefig("terminal-v.png", dpi=300, bbox_inches='tight')
plt.show()



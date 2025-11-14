import numpy as np
import matplotlib.pyplot as plt
import scienceplots

v0 = 0
t0 = 0
g = 9.8
dt = 0.1
tf = 10

vs_euler= []
ts = []
v = v0
t = t0

while t <= tf:
    vs_euler.append(v)
    ts.append(t)
    v = v - g * dt
    t += dt


ts_exact = np.linspace(0, tf, 200)
vs_exact = -g*ts_exact

plt.style.use(['science', 'grid', 'bright'])
plt.figure(figsize=(6,4))
plt.plot(ts, vs_euler, '-', label='Euler Approx.', lw=2)
plt.plot(ts_exact, vs_exact, '--', label='Exact Solution', lw=2)
plt.xlabel('Time(s)')
plt.ylabel('Velocity (m/s)')
plt.title('Free Fall (Euler vs. Exact)')
plt.legend()
plt.savefig("free-fall.png", dpi=300, bbox_inches='tight')
plt.show()

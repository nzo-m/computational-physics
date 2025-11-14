import numpy as np
import matplotlib.pyplot as plt
import scienceplots

NA0=1000
NB0=0
dt=0.01
tf=5
ts=np.arange(0,tf+dt,dt)

ta=[1,0.5,1]
tb=[0.5,1,1]

plt.style.use(['science','grid','bright'])
fig, axes = plt.subplots(1, 3, figsize=(15,4))
fig.suptitle("Radioactive Decay with Varying Ratios")

for i in range(3):
    NA = np.zeros_like(ts, dtype=float)
    NB = np.zeros_like(ts, dtype=float)

    NA[0] = NA0
    NB[0] = NB0

    for j in range(len(ts)-1):
        dNA = -NA[j]/ta[i]
        dNB = NA[j]/ta[i] - NB[j]/tb[i]
        NA[j+1] = NA[j] + dNA*dt
        NB[j+1] = NB[j] + dNB*dt

    ax = axes[i]
    ax.plot(ts, NA, label="NA")
    ax.plot(ts, NB, label="NB")

    ax.set_title(f"TA/TB = {ta[i]}/{tb[i]}")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Atoms")
    ax.legend()

plt.savefig("radioactive-decay.png", dpi=300, bbox_inches='tight')
plt.show()
